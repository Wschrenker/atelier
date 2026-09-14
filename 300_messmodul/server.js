// Schlanker Server nur fuer das Brautkleid-Messmodul: statische Dateien
// aus diesem Ordner plus die Braut-API, die brautkleid-messmodul.js aufruft.
// Kein Muster-Export, kein Grundformen-Auswahlbildschirm — die wurden
// bewusst nicht mitkopiert.
import { createReadStream } from "node:fs";
import http from "node:http";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { brideStore } from "./src/bridal/bride-store.js";

const appRoot = path.dirname(fileURLToPath(import.meta.url));
const port = Number(process.env.PORT || 3301);

const mimeTypes = {
  ".html": "text/html; charset=utf-8",
  ".css": "text/css; charset=utf-8",
  ".js": "application/javascript; charset=utf-8",
  ".json": "application/json; charset=utf-8",
  ".svg": "image/svg+xml; charset=utf-8"
};

function send(res, status, body, type = "text/plain; charset=utf-8") {
  res.writeHead(status, { "Content-Type": type, "Cache-Control": "no-store" });
  res.end(body);
}

function sendJson(res, status, body) {
  send(res, status, `${JSON.stringify(body, null, 2)}\n`, "application/json; charset=utf-8");
}

function isInsideBase(candidate, base) {
  const relative = path.relative(base, candidate);
  return relative === "" || (!relative.startsWith("..") && !path.isAbsolute(relative));
}

function safeStaticPath(urlPath) {
  const cleanPath = decodeURIComponent(urlPath.split("?")[0]);
  const relativePath = cleanPath === "/" ? "brautkleid-messmodul.html" : cleanPath.replace(/^\//, "");
  const candidate = path.resolve(appRoot, relativePath);
  return isInsideBase(candidate, appRoot) ? candidate : null;
}

function readJsonBody(req) {
  return new Promise((resolve, reject) => {
    let body = "";
    req.on("data", (chunk) => {
      body += chunk;
      if (body.length > 1024 * 1024) {
        reject(new Error("request body too large"));
        req.destroy();
      }
    });
    req.on("end", () => {
      try {
        resolve(body ? JSON.parse(body) : {});
      } catch (error) {
        reject(error);
      }
    });
    req.on("error", reject);
  });
}

async function handleApi(req, res, urlPath) {
  if (req.method === "GET" && urlPath === "/api/brides") {
    sendJson(res, 200, await brideStore.listBrides());
    return true;
  }
  if (req.method === "POST" && urlPath === "/api/brides") {
    const payload = await readJsonBody(req);
    sendJson(res, 200, await brideStore.saveBride(payload));
    return true;
  }
  if (urlPath.startsWith("/api/brides/")) {
    const brideId = urlPath.slice("/api/brides/".length);
    if (req.method === "GET") {
      const bride = await brideStore.getBride(brideId);
      sendJson(res, bride ? 200 : 404, bride || { error: "Braut nicht gefunden." });
      return true;
    }
    if (req.method === "DELETE") {
      const deleted = await brideStore.deleteBride(brideId);
      sendJson(res, deleted ? 200 : 404, deleted ? { deleted: true } : { error: "Braut nicht gefunden." });
      return true;
    }
  }
  return false;
}

const server = http.createServer(async (req, res) => {
  const urlPath = decodeURIComponent((req.url || "/").split("?")[0]);
  if (urlPath.startsWith("/api/")) {
    try {
      const handled = await handleApi(req, res, urlPath);
      if (!handled) sendJson(res, 404, { error: "Not found" });
    } catch (error) {
      sendJson(res, 400, { error: error.message });
    }
    return;
  }

  const filePath = safeStaticPath(req.url || "/");
  if (!filePath) {
    send(res, 403, "Forbidden");
    return;
  }

  createReadStream(filePath)
    .on("error", () => send(res, 404, "Not found"))
    .on("open", () => {
      const ext = path.extname(filePath).toLowerCase();
      res.writeHead(200, {
        "Content-Type": mimeTypes[ext] || "application/octet-stream",
        "Cache-Control": "no-store"
      });
    })
    .pipe(res);
});

server.listen(port, "127.0.0.1", () => {
  console.log(`Messmodul: http://127.0.0.1:${port}`);
});

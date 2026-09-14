const EPSILON = 1e-8;

export function point(x, y) {
  return { x, y };
}

export function closePolygon(points) {
  if (points.length === 0) return [];
  const first = points[0];
  const last = points.at(-1);
  if (Math.abs(first.x - last.x) < EPSILON && Math.abs(first.y - last.y) < EPSILON) {
    return points.map(({ x, y }) => point(x, y));
  }
  return [...points.map(({ x, y }) => point(x, y)), point(first.x, first.y)];
}

export function polygonArea(points) {
  const closed = closePolygon(points);
  let area = 0;
  for (let i = 0; i < closed.length - 1; i += 1) {
    area += closed[i].x * closed[i + 1].y - closed[i + 1].x * closed[i].y;
  }
  return area / 2;
}

function lineIntersection(a, b, c, d) {
  const ab = point(b.x - a.x, b.y - a.y);
  const cd = point(d.x - c.x, d.y - c.y);
  const divisor = ab.x * cd.y - ab.y * cd.x;
  if (Math.abs(divisor) < EPSILON) return point(b.x, b.y);
  const ac = point(c.x - a.x, c.y - a.y);
  const t = (ac.x * cd.y - ac.y * cd.x) / divisor;
  return point(a.x + t * ab.x, a.y + t * ab.y);
}

function offsetSegment(a, b, distance, orientation) {
  const dx = b.x - a.x;
  const dy = b.y - a.y;
  const length = Math.hypot(dx, dy);
  if (length < EPSILON) return [point(a.x, a.y), point(b.x, b.y)];
  const direction = orientation >= 0 ? 1 : -1;
  const nx = direction * dy / length;
  const ny = direction * -dx / length;
  return [
    point(a.x + nx * distance, a.y + ny * distance),
    point(b.x + nx * distance, b.y + ny * distance)
  ];
}

export function offsetPolygon(points, allowances) {
  const polygon = closePolygon(points).slice(0, -1);
  if (polygon.length < 3 || allowances.length !== polygon.length) {
    throw new Error("offsetPolygon needs one allowance per polygon edge");
  }
  const orientation = polygonArea(polygon);
  const segments = polygon.map((current, index) => (
    offsetSegment(current, polygon[(index + 1) % polygon.length], allowances[index], orientation)
  ));
  const shifted = segments.map((segment, index) => {
    const previous = segments[(index - 1 + segments.length) % segments.length];
    return lineIntersection(previous[0], previous[1], segment[0], segment[1]);
  });
  return closePolygon(shifted);
}

export function sampleQuadratic(start, control, end, steps = 6) {
  const sampled = [];
  for (let i = 0; i <= steps; i += 1) {
    const t = i / steps;
    const inv = 1 - t;
    sampled.push(point(
      inv * inv * start.x + 2 * inv * t * control.x + t * t * end.x,
      inv * inv * start.y + 2 * inv * t * control.y + t * t * end.y
    ));
  }
  return sampled;
}

export function boundsOfDocument(document) {
  const all = document.pieces.flatMap((piece) => piece.cuttingLine);
  return {
    minX: Math.min(...all.map((item) => item.x)),
    minY: Math.min(...all.map((item) => item.y)),
    maxX: Math.max(...all.map((item) => item.x)),
    maxY: Math.max(...all.map((item) => item.y))
  };
}

export function translatePoints(points, dx, dy) {
  return points.map(({ x, y }) => point(x + dx, y + dy));
}

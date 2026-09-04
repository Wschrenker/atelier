"""Prüft, ob alle Dateiverweise im Repo noch auf vorhandene Dateien zeigen.

Warum es das gibt: Wenn eine Datei auf eine andere verweist, die gelöscht oder
umbenannt wurde, entsteht eine Lücke. Ein Mensch sieht sie nicht, und ein
Sprachmodell fängt an, den fehlenden Inhalt zu raten. Dieses Skript findet
solche Lücken mechanisch, damit Umräumen und Löschen ungefährlich wird.

Aufruf:  python 600_prozess/werkzeuge/verweise_pruefen.py
Rückgabe: 0 = alles heil, 1 = mindestens ein toter Verweis.
"""

import pathlib
import re
import sys

WURZEL = pathlib.Path(__file__).resolve().parents[2]

# Ordner, die nie geprüft werden: Fotos und Werkzeugablagen.
UEBERSPRINGEN = {".git", ".hermes", "__pycache__", ".pytest_cache", "2_bilder"}

# 1) [Text](pfad)  2) `pfad.md` in Backticks  3) Quelle:/Datei: pfad
MUSTER_LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
MUSTER_BACKTICK = re.compile(r"`([^`\n]+?\.(?:md|py|jpg|json))`")


def dateien():
    for p in WURZEL.rglob("*.md"):
        if not UEBERSPRINGEN & set(p.relative_to(WURZEL).parts):
            yield p


def kandidaten(text):
    for m in MUSTER_LINK.finditer(text):
        yield m.group(1).strip()
    for m in MUSTER_BACKTICK.finditer(text):
        yield m.group(1).strip()


# Platzhalter wie `s<Seite>.md` sind Schreibmuster, keine echten Verweise.
MUSTER_PLATZHALTER = re.compile(r"[<>{}]|\.\.\.")


def aufloesen(ziel, quelle):
    """Gibt 'ok'/'extern'/'platzhalter'/'bild' zurück, oder None bei totem Verweis."""
    ziel = ziel.split("#")[0].strip()
    if not ziel or ziel.startswith(("http://", "https://", "mailto:")):
        return "extern"
    if MUSTER_PLATZHALTER.search(ziel):
        return "platzhalter"

    # Absoluter Windows-Pfad im Text, z. B. C:\ATELIER\...
    if re.match(r"^[A-Za-z]:[\/]", ziel):
        p = pathlib.Path(ziel)
        return "ok" if p.exists() else None

    ziel = ziel.replace("\\", "/").lstrip("/")

    for basis in (quelle.parent, WURZEL):
        if (basis / ziel).exists():
            return "ok"

    # Nur ein Dateiname ohne Pfad: irgendwo im Repo suchen.
    if "/" not in ziel:
        if next(WURZEL.rglob(ziel), None) is not None:
            return "ok"

    # Fotos liegen absichtlich außerhalb der Versionierung.
    if ziel.lower().endswith((".jpg", ".jpeg", ".png")):
        return "bild"
    return None


def main():
    tot = []
    geprueft = 0
    bilder = 0
    anzahl_dateien = 0
    for quelle in dateien():
        anzahl_dateien += 1
        text = quelle.read_text(encoding="utf-8", errors="replace")
        for ziel in set(kandidaten(text)):
            geprueft += 1
            art = aufloesen(ziel, quelle)
            if art == "bild":
                bilder += 1
            elif art is None:
                tot.append((quelle.relative_to(WURZEL).as_posix(), ziel))

    print(f"{geprueft} Verweise geprüft in {anzahl_dateien} Dateien.")
    if bilder:
        print(f"{bilder} Bildverweise übersprungen (Fotos liegen außerhalb des Repos).")
    if not tot:
        print("Alle Verweise zeigen auf vorhandene Dateien.")
        return 0

    print(f"\n{len(tot)} tote Verweise:\n")
    letzte = None
    for datei, ziel in sorted(tot):
        if datei != letzte:
            print(f"  {datei}")
            letzte = datei
        print(f"      -> {ziel}")
    return 1


if __name__ == "__main__":
    sys.exit(main())

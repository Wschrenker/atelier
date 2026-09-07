# -*- coding: utf-8 -*-
"""Erzeugt die Arbeitsansicht `pruefstellen_nach_seiten/` aus den Quellen.

Die fuenf Zusammenzuege im Archiv sind die einzige Stelle, an der ein
Pruefstellen-Status geaendert wird. Dieses Skript verteilt sie auf
Buchseiten und schreibt je Seite eine Datei. Die Ansicht ist damit
jederzeit neu erzeugbar und wird nie von Hand gepflegt.

    python pruefstellen_ansicht_bauen.py            Probelauf, meldet Abweichungen
    python pruefstellen_ansicht_bauen.py --schreiben Ansicht neu schreiben

Die Seitentranskriptionen `sNNN.md` und die urspruenglichen
`formeln_sNNN.md` werden nicht angefasst.
"""
from __future__ import unicode_literals

import codecs
import io
import os
import re
import shutil
import sys

WURZEL = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
ARCHIV = os.path.join(WURZEL, "100_quellen", "30_hofenbitzer_band_1_archiv")
ZIEL = os.path.join(WURZEL, "100_quellen", "10_hofenbitzer_band_1_digital",
                    "pruefstellen_nach_seiten")

FORMELN = "prüfstelle_formel_zusammenzug"
TEXTE = "prüfstelle_text_zusammenzug"

# Buchkategorien: (Ordner, Anzeigename, erste Seite, letzte Seite)
KAPITEL = [
    ("00_vorspann_s1-7", "Vorspann", 1, 7),
    ("01_grundlagen_s8-31", "Grundlagen", 8, 31),
    ("02_grundschnitte_roecke_s32-39", "Grundschnitte Röcke", 32, 39),
    ("03_modelle_roecke_s40-105", "Modelle Röcke", 40, 105),
    ("04_grundschnitte_hosen_s106-137", "Grundschnitte Hosen", 106, 137),
    ("05_modelle_hosen_s138-170", "Modelle Hosen", 138, 170),
    ("06_grundschnitte_oberteile_s171-196", "Grundschnitte Oberteile", 171, 196),
    ("07_grundschnitte_aermel_s197-220", "Grundschnitte Ärmel", 197, 220),
    ("08_aermel_varianten_s221-289", "Ärmel-Varianten", 221, 289),
    ("09_kragen_kapuzen_taschen_s290-369", "Kragen, Kapuzen und Taschen", 290, 369),
    ("10_ausschnitte_s370-437", "Ausschnitte", 370, 437),
    ("11_modelle_kleider_blusen_westen_s438-464",
     "Modelle Kleider, Blusen, Westen", 438, 464),
    ("12_modelle_jacken_s465-492", "Modelle Jacken", 465, 492),
    ("13_sportswear_waesche_unisex_s493-534",
     "Sportswear, Wäsche, Unisex", 493, 534),
    ("14_anhang_sachwortverzeichnis_s535-544",
     "Anhang und Sachwortverzeichnis", 535, 544),
]

# (Schluessel, Rubriktitel, Unterordner, Dateiname, Zerlegeart)
QUELLEN = [
    ("formel_pruefabschnitte", "Formel-Prüfabschnitte",
     FORMELN, "00_pruefstellen_formeln_band_1.md", "abschnitt"),
    ("formel_offene_fragen", "Offene Fragen in normalisierten Formeln",
     FORMELN, "01_offene_fragen_normalisierte_formeln.md", "seitenblock"),
    ("text_erste_pruefung", "Text-Prüfstellen der ersten Zweitprüfung",
     TEXTE, "00_pruefstellen_text_band_1_zusammenzug.md", "punkt"),
    ("text_abweichungen", "Abweichungen der Transkription vom Foto (D)",
     TEXTE, "01_abweichungen_transkript_vom_foto.md", "eintrag"),
    ("text_buchfehler", "Buchfehler aus dem Archiv-Prüfstand (A/B/C)",
     TEXTE, "02_buchfehler_aus_dem_archiv.md", "eintrag"),
]

OHNE_SEITE = "Ohne Seitenangabe im Eintragskopf"


def lies(pfad):
    with io.open(pfad, encoding="utf-8") as f:
        return f.read().replace("\r\n", "\n").split("\n")


def seiten_aus(text):
    """Seitenzahlen aus einer Angabe wie 'S. 116-118, 120-123' oder 'S.33'."""
    treffer = re.search(r"S\.\s*([0-9][0-9.,–—\-\s]*)", text)
    if not treffer:
        return []
    rest = treffer.group(1)
    rest = re.split(r"\s—\s|\s–\s(?=[A-Z])", rest)[0]
    gefunden = []
    for stueck in rest.split(","):
        stueck = stueck.strip()
        spanne = re.match(r"^(\d+)(?:\.\d+)?\s*[–—-]\s*(\d+)$", stueck)
        einzel = re.match(r"^(\d+)(?:\.\d+)?$", stueck)
        if spanne:
            von, bis = int(spanne.group(1)), int(spanne.group(2))
            if von <= bis <= von + 200:
                gefunden.extend(range(von, bis + 1))
        elif einzel:
            gefunden.append(int(einzel.group(1)))
    return gefunden


def alle_seiten(text):
    """Jede genannte Seite, Spannen aufgeloest.

    Aufzaehlungspunkte schreiben Spannen aus: 'erledigt für S.200–213'
    meint jede Seite von 200 bis 213.
    """
    gefunden = []
    for von, bis in re.findall(r"S\.\s*(\d+)(?:\s*[–—-]\s*(\d+))?", text):
        erste = int(von)
        letzte = int(bis) if bis else erste
        if erste <= letzte <= erste + 200:
            for seite in range(erste, letzte + 1):
                if seite not in gefunden:
                    gefunden.append(seite)
    return gefunden


def literale_seiten(text):
    """Nur die woertlich genannten Seitenzahlen, ohne Spannen aufzuloesen.

    Eintragskoepfe wie '(16. Durchgang, S.341 und S.342–S.346) · auch S.344'
    meinen die genannten Seiten selbst, nicht jede dazwischen. Der Punkt
    steht also auf S.341, S.342, S.344 und S.346.
    """
    gefunden = []
    for zahl in re.findall(r"S\.\s*(\d+)", text):
        seite = int(zahl)
        if seite not in gefunden:
            gefunden.append(seite)
    return gefunden


def block_text(zeilen):
    """Fuehrende und abschliessende Leerzeilen entfernen."""
    while zeilen and not zeilen[0].strip():
        zeilen = zeilen[1:]
    while zeilen and not zeilen[-1].strip():
        zeilen = zeilen[:-1]
    return "\n".join(zeilen)


def zerlege_abschnitt(zeilen):
    """Einheit = ein '### S. ... - Kuerzel' Block. Seiten aus der Ueberschrift."""
    einheiten = []
    kopf, puffer = None, []
    for zeile in zeilen:
        if zeile.startswith("### "):
            if kopf is not None:
                einheiten.append((seiten_aus(kopf), block_text([kopf] + puffer)))
            kopf, puffer = zeile, []
        elif zeile.startswith("## ") or zeile.startswith("# "):
            if kopf is not None:
                einheiten.append((seiten_aus(kopf), block_text([kopf] + puffer)))
            kopf, puffer = None, []
        elif kopf is not None:
            puffer.append(zeile)
    if kopf is not None:
        einheiten.append((seiten_aus(kopf), block_text([kopf] + puffer)))
    return einheiten


def zerlege_seitenblock(zeilen):
    """Wie 'abschnitt', aber erst ab '# Die Fragen nach Buchseite'."""
    ab = 0
    for i, zeile in enumerate(zeilen):
        if re.match(r"^# Die (Fragen|Punkte) nach Buchseite", zeile):
            ab = i + 1
            break
    return zerlege_abschnitt(zeilen[ab:])


def kopfseiten(text):
    """Seiten aus dem fett gesetzten Eintragskopf, der ueber Zeilen laufen kann.

    'S.182/S.183' und 'S.207, S.208 und S.211' nennen mehrere Seiten; der
    Punkt steht dann auf jeder davon.
    """
    fett = re.match(r"^- \*\*(.*?)\*\*", text, re.S)
    return alle_seiten(fett.group(1)) if fett else seiten_aus(text)


def zerlege_punkt(zeilen):
    """Einheit = ein Aufzaehlungspunkt '- **... :**'. Seiten aus dem Fettkopf."""
    einheiten = []
    kopf, puffer = None, []

    def schliesse():
        if kopf is None:
            return
        text = block_text([kopf] + puffer)
        einheiten.append((kopfseiten(text), text))

    for zeile in zeilen:
        if re.match(r"^- \*\*", zeile):
            schliesse()
            kopf, puffer = zeile, []
        elif zeile.startswith("#"):
            schliesse()
            kopf, puffer = None, []
        elif kopf is not None:
            if zeile.strip() and not zeile.startswith((" ", "\t", ">")):
                schliesse()
                kopf, puffer = None, []
            else:
                puffer.append(zeile)
    schliesse()
    return einheiten


EINTRAGSKOPF = re.compile(r"^\*\*[A-Za-z]+\d+[^*]* — [^*]+\*\*(.*)$")


def zerlege_eintrag(zeilen):
    """Einheit = '**D1 - offen**' bis zum naechsten Eintrag.

    Heimatseite ist die umgebende '### S.107' Ueberschrift. Mehrseitige
    Punkte tragen im Kopf schon den Zusatz '· auch S.108, S.111' und stehen
    dann auf allen dort genannten Seiten mit. Im Abschnitt 'Ohne
    Seitenangabe im Eintragskopf' bleibt die Einheit ohne Seite.
    """
    ab = 0
    for i, zeile in enumerate(zeilen):
        if re.match(r"^# Die (Fragen|Punkte) nach Buchseite", zeile):
            ab = i + 1
            break

    einheiten = []
    seiten, zusatz, kopf, puffer, ohne = [], [], None, [], False

    def schliesse():
        if kopf is None:
            return
        if ohne:
            eigene = []
        else:
            eigene = list(seiten)
            for s in zusatz:
                if s not in eigene:
                    eigene.append(s)
        einheiten.append((eigene, block_text([kopf] + puffer)))

    for zeile in zeilen[ab:]:
        if zeile.startswith("## "):
            schliesse()
            kopf, puffer = None, []
            ohne = OHNE_SEITE in zeile
            seiten = []
        elif zeile.startswith("### "):
            schliesse()
            kopf, puffer = None, []
            seiten = seiten_aus(zeile)
        elif EINTRAGSKOPF.match(zeile):
            schliesse()
            kopf, puffer = zeile, []
            zusatz = literale_seiten(zeile)
        elif kopf is not None:
            puffer.append(zeile)
    schliesse()
    return einheiten


ZERLEGER = {
    "abschnitt": zerlege_abschnitt,
    "seitenblock": zerlege_seitenblock,
    "punkt": zerlege_punkt,
    "eintrag": zerlege_eintrag,
}


def kapitel_fuer(seite):
    for ordner, name, von, bis in KAPITEL:
        if von <= seite <= bis:
            return ordner, name
    return None, None


def einlesen():
    """Alle Quellen zerlegen. Liefert Einheiten je Rubrik in Dokumentfolge."""
    alles = []
    for schluessel, titel, unterordner, datei, art in QUELLEN:
        pfad = os.path.join(ARCHIV, unterordner, datei)
        if not os.path.isfile(pfad):
            sys.stderr.write("Quelle fehlt: %s\n" % pfad)
            sys.exit(1)
        einheiten = ZERLEGER[art](lies(pfad))
        nummeriert = []
        for lauf, (seiten, text) in enumerate(einheiten, start=1):
            nummeriert.append({
                "schluessel": schluessel,
                "titel": titel,
                "id": "%s:%04d" % (schluessel, lauf),
                "seiten": seiten,
                "text": text,
                "quelle": "%s/%s" % (unterordner, datei),
            })
        alles.append((schluessel, titel, unterordner, datei, nummeriert))
    return alles


def links_umhaengen(text, stufen, quellordner):
    """Relative Links im Eintragstext auf den neuen Ablageort umrechnen.

    Der Wortlaut bleibt unveraendert; nur die Pfade werden nachgezogen,
    damit ein aus der Quelle uebernommener Link weiterhin zielt. Zwei Faelle:
    `../..`-Pfade brauchen eine Stufe mehr, und ein blosser Dateiname meint
    ein Geschwister der Quelldatei und bekommt deren Ordner davor.
    """
    zurueck = "../" * (stufen + 2)

    def ersetze(treffer):
        klammer, ziel = treffer.group(1), treffer.group(2)
        if ziel.startswith("../"):
            return "](%s%s%s" % (klammer, "../" * stufen, ziel)
        if re.match(r"^(https?:|#|/|<?\.\.?/)", ziel):
            return treffer.group(0)
        return "](%s%s30_hofenbitzer_band_1_archiv/%s/%s" % (
            klammer, zurueck, quellordner, ziel)

    return re.sub(r"\]\((<?)([^)>]+)", ersetze, text)


def rubrik_block(titel, unterordner, datei, einheiten, tiefe):
    hoch = "../" * tiefe
    zeilen = ["## %s" % titel, "",
              "Quelle: [`%s/%s`](%s30_hofenbitzer_band_1_archiv/%s/%s)"
              % (unterordner, datei, hoch, unterordner, datei), ""]
    for i, einheit in enumerate(einheiten):
        if i:
            zeilen.extend(["---", ""])
        zeilen.append("<!-- einheit: %s -->" % einheit["id"])
        zeilen.append(links_umhaengen(einheit["text"], tiefe - 2, unterordner))
        zeilen.append("")
    return zeilen


def seite_bauen(seite, rubriken):
    kategorie = kapitel_fuer(seite)[1]
    zeilen = ["# Prüfstellen — Buchseite S. %d" % seite, "",
              "> Abgeleitete Arbeitsansicht. Die Originaldateien bleiben "
              "unverändert.", "",
              "**Buchkategorie:** %s" % kategorie, "",
              "## Inhalt", ""]
    for titel, _, _, einheiten in rubriken:
        zeilen.append("- %s: %d" % (titel, len(einheiten)))
    zeilen.append("")
    for titel, unterordner, datei, einheiten in rubriken:
        zeilen.extend(rubrik_block(titel, unterordner, datei, einheiten, 3))
    return "\n".join(zeilen).rstrip() + "\n"


def bauen():
    alles = einlesen()

    nach_seite = {}
    ohne_seite = []
    for schluessel, titel, unterordner, datei, einheiten in alles:
        for einheit in einheiten:
            if not einheit["seiten"]:
                ohne_seite.append((titel, unterordner, datei, einheit))
                continue
            for seite in einheit["seiten"]:
                if kapitel_fuer(seite)[0] is None:
                    continue
                nach_seite.setdefault(seite, []).append(
                    (titel, unterordner, datei, einheit))

    dateien = {}
    for seite in sorted(nach_seite):
        rubriken = []
        for _, titel, unterordner, datei, _ in alles:
            passend = [e for t, u, d, e in nach_seite[seite] if t == titel]
            if passend:
                rubriken.append((titel, unterordner, datei, passend))
        ordner = kapitel_fuer(seite)[0]
        dateien["%s/s%03d.md" % (ordner, seite)] = seite_bauen(seite, rubriken)

    if ohne_seite:
        zeilen = ["# Prüfstellen ohne eindeutige Seitenzuordnung", "",
                  "> Diese Einträge stehen in den Quellen ausdrücklich "
                  "unter „Ohne Seitenangabe im Eintragskopf“ und wurden "
                  "deshalb keiner Buchseite zugeschlagen.", ""]
        for _, titel, unterordner, datei, _ in alles:
            passend = [e for t, u, d, e in ohne_seite if t == titel]
            if passend:
                zeilen.extend(rubrik_block(titel, unterordner, datei,
                                           passend, 2))
        dateien["ohne_eindeutige_seitenzuordnung.md"] = \
            "\n".join(zeilen).rstrip() + "\n"

    return dateien


def vergleiche(dateien):
    vorhanden = set()
    for wurzel, _, namen in os.walk(ZIEL):
        for name in namen:
            if name.endswith(".md") and name != "README.md":
                p = os.path.relpath(os.path.join(wurzel, name), ZIEL)
                vorhanden.add(p.replace("\\", "/"))
    neu = set(dateien)
    gleich = abweichend = 0
    for pfad in sorted(neu & vorhanden):
        with io.open(os.path.join(ZIEL, pfad), encoding="utf-8") as f:
            alt = f.read().replace("\r\n", "\n")
        if alt == dateien[pfad]:
            gleich += 1
        else:
            abweichend += 1
    return {
        "gleich": gleich,
        "abweichend": abweichend,
        "nur_neu": sorted(neu - vorhanden),
        "nur_alt": sorted(vorhanden - neu),
    }


def schreiben(dateien):
    for ordner, _, _, _ in KAPITEL:
        p = os.path.join(ZIEL, ordner)
        if os.path.isdir(p):
            shutil.rmtree(p)
    for pfad, inhalt in dateien.items():
        ziel = os.path.join(ZIEL, pfad.replace("/", os.sep))
        verzeichnis = os.path.dirname(ziel)
        if verzeichnis and not os.path.isdir(verzeichnis):
            os.makedirs(verzeichnis)
        with codecs.open(ziel, "w", "utf-8") as f:
            f.write(inhalt)


def main():
    dateien = bauen()
    print("Erzeugt: %d Dateien" % len(dateien))

    ergebnis = vergleiche(dateien)
    print("Deckungsgleich mit dem Bestand: %d" % ergebnis["gleich"])
    print("Inhaltlich abweichend:          %d" % ergebnis["abweichend"])
    print("Nur neu erzeugt:                %d" % len(ergebnis["nur_neu"]))
    print("Nur im Bestand:                 %d" % len(ergebnis["nur_alt"]))
    for pfad in ergebnis["nur_neu"][:10]:
        print("   + %s" % pfad)
    for pfad in ergebnis["nur_alt"][:10]:
        print("   - %s" % pfad)

    if "--schreiben" in sys.argv:
        schreiben(dateien)
        print("\nAnsicht neu geschrieben.")
    else:
        print("\n[Probelauf - nichts geschrieben. Mit --schreiben ausfuehren.]")


if __name__ == "__main__":
    main()

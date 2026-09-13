"""Kleid v002 "Lumiere" - Schnitt bauen und als DXF ausgeben.

Dieses Skript **besitzt keine Konstruktion**. Es waehlt Module aus
`500_python/10_rechnung/` aus, verknuepft sie und trifft die Entscheidungen,
die nur dieses Kleid betreffen. Alles, was ein zweites Kleid auch braeuchte,
gehoert nach unten - nicht hierher.

Aufruf:

    python 700_schnitte/20_kleid_lumiere/bauen.py

Ergebnis: `ausgabe/kleid_lumiere_gr38.dxf` und ein Protokoll auf der Konsole.

Lies vor dem Zuschneiden `DEFINITION.md` - dort steht, welche Zahl aus dem Buch
stammt und welche eine Modellentscheidung ist.
"""

from __future__ import annotations

import sys
from pathlib import Path

WURZEL = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(WURZEL / "500_python" / "10_rechnung"))

from geometrie import (  # noqa: E402
    Punkt, cm, mm_zu_cm, polylinie_laenge, spiegle_alle, spiegle_senkrecht,
    schnitt_mit_waagerechter,
)
from masse import koerpermasse  # noqa: E402
from oberteil import konstruktionstabelle, grundgeruest, tailliert  # noqa: E402
from rock import konstruktionstabelle_rock, gerader_rock, saumerweitert  # noqa: E402
from schnitt import schneide_halbebene  # noqa: E402
from ausgabe import Schnittteil, schreibe_dxf  # noqa: E402


# ============================================================================
# Entscheidungen dieses Kleides. Jede Zeile ist in DEFINITION.md begruendet.
# ============================================================================

GROESSE = 38

# --- gemeinsame Taille: Rock und Oberteil muessen an der Naht zusammenpassen
TAILLEN_ZUGABE_CM = 2.0        # Buch S.33 Spanne 1-2 fuer den Rock; hier auch fuer das OT
VABL_ZUGABE_CM = 1.0           # S.184 Schritt 36, Spanne "+0 bis 1 cm", bis PK 4 -> 1,0

# --- Rock
ROCK_LAENGE_CM = 106.0         # sTaH Gr.38 = 106 -> an der Seite bodenlang
SAUMERWEITERUNG_CM = 90.0      # Modellentscheidung, S.43 rechnet daraus 6 Keile
SCHLITZ_HOEHE_CM = 62.0        # Modellentscheidung: Beinschlitz an der vM

# --- Oberteil, asymmetrische Gestaltung (S.423, ohne Buchzahlen)
RUECKEN_V_UEBER_TAILLE_CM = 6.0   # Spitze des Rueckenausschnitts oberhalb der Taille
HABL_LAENGE_CM = 10.0             # S.185 Abb. 8c: "zum Naehen auf ca. 10 cm gekuerzt"
WICKELKANTE_SEITE_CM = 7.0        # Ausschnittkante an der linken SN, unter der Brustlinie
UNTERTRITT_SEITE_CM = 1.0         # Oberkante Untertritt an der linken SN, unter der Brustlinie
UNTERTRITT_VM_CM = -4.0           # Oberkante Untertritt an der vM (negativ = ueber der Brustlinie)
SCHULTERABNAEHER_CM = 0.0         # entfaellt: der offene Rueckenausschnitt schneidet ihn ohnehin weg


def _behalte_mit(kontur, a: Punkt, b: Punkt, referenz: Punkt):
    """Schneidet an der Geraden a-b und behaelt die Seite, auf der `referenz` liegt."""
    kreuz = (b[0] - a[0]) * (referenz[1] - a[1]) - (b[1] - a[1]) * (referenz[0] - a[0])
    return schneide_halbebene(kontur, a, b, behalte_positiv=kreuz >= 0)


def _innerhalb(punkte, a: Punkt, b: Punkt, referenz: Punkt) -> bool:
    """Liegen alle Punkte auf derselben Seite der Geraden wie `referenz`?"""
    def seite(p):
        return (b[0] - a[0]) * (p[1] - a[1]) - (b[1] - a[1]) * (p[0] - a[0])
    soll = seite(referenz) >= 0
    return all((seite(p) >= 0) == soll for p in punkte)


def _gekuerzt(ab, a: Punkt, b: Punkt, referenz: Punkt, mindest_cm: float = 5.0):
    """Kuerzt einen Abnaeher so, dass seine Spitze im beschnittenen Teil bleibt.

    Ein Ausschnitt kann eine Abnaeherspitze abschneiden. Statt den Abnaeher
    stillschweigend zu zerstoeren, wird er gekuerzt - und wenn dafuer kein Platz
    mehr ist, ganz weggelassen.
    """
    from geometrie import abstand, schnitt_gerade_gerade
    if _innerhalb([ab.spitze], a, b, referenz):
        return ab, None
    mitte = ((ab.schenkel_a[0] + ab.schenkel_b[0]) / 2.0,
             (ab.schenkel_a[1] + ab.schenkel_b[1]) / 2.0)
    treffer = schnitt_gerade_gerade(mitte, ab.spitze, a, b)
    richtung = 1.0 if ab.spitze[1] < mitte[1] else -1.0
    neue = (treffer[0], treffer[1] - richtung * cm(1.5))
    laenge = abstand(mitte, neue)
    if laenge < cm(mindest_cm):
        return None, (f"{ab.name}: der Ausschnitt laeszt nur "
                      f"{mm_zu_cm(laenge):.1f} cm Abnaeherlaenge - weggelassen. "
                      "Der Inhalt musz anders untergebracht werden.")
    gekuerzt = type(ab)(ab.name, ab.schenkel_a, neue, ab.schenkel_b, ab.inhalt_cm)
    return gekuerzt, (f"{ab.name} auf {mm_zu_cm(laenge):.1f} cm gekuerzt, "
                      "damit die Spitze im Ausschnitt bleibt.")


def _fadenlauf(teil: Schnittteil, x: float, y_von: float, y_bis: float) -> None:
    teil.hilfslinie([(x, y_von), (x, y_bis)], "FADENLAUF")
    teil.hilfslinie([(x - cm(1.0), y_bis - cm(2.0)), (x, y_bis),
                     (x + cm(1.0), y_bis - cm(2.0))], "FADENLAUF")


def bauen(ziel: Path) -> None:
    m = koerpermasse(GROESSE)
    protokoll: list[str] = []

    def sag(zeile: str = "") -> None:
        protokoll.append(zeile)
        print(zeile)

    sag(f"Kleid Lumiere - Referenzgroesze {GROESSE}")
    sag("=" * 62)

    # ------------------------------------------------------------ Oberteil
    t_ot = konstruktionstabelle(m, zg_TaU=TAILLEN_ZUGABE_CM)
    sag(f"Oberteil S.177  BrW {t_ot.BrW}  1/2 {t_ot.halb_BrW}  "
        f"Kontrolle RueB+ + ArD+ + BrB+ - 1/2 BrW = {t_ot.kontrolle_brustweite()}")
    sag(f"                TaW {t_ot.TaW}  1/2 {t_ot.halb_TaW}   "
        f"individuelle Balance {t_ot.individuelle_balance} (optimal 3,5)")

    gg = grundgeruest(t_ot)
    ot = tailliert(gg, vabl_zugabe_cm=VABL_ZUGABE_CM,
                   schulterabnaeher_cm=SCHULTERABNAEHER_CM,
                   hAbl_laenge_cm=HABL_LAENGE_CM)
    sag(f"S.184  me {ot.me_cm} cm -> vAbl {ot.vAbl_cm} cm")
    sag(f"S.184  vTaB {ot.vTaB_cm} + hTaB {ot.hTaB_cm} - 1/2 TaW {t_ot.halb_TaW} "
        f"= TaAf {ot.TaAf_cm} cm")
    sag(f"S.185  Aufteilung: SN {ot.sn_cm} + shAbl {ot.shAbl_cm} + hAbl {ot.hAbl_cm}")
    sag(f"S.184  Brustabnaeher: {ot.brustabnaeher_grad:.1f} Grad Drehung um den BrP "
        f"- NUR als Konstruktionslinie eingezeichnet, siehe DEFINITION.md")
    for h in ot.hinweise:
        sag(f"       ! {h}")

    # ---------------------------------------------------------------- Rock
    t_rk = konstruktionstabelle_rock(
        m, zg_TaU=TAILLEN_ZUGABE_CM, MoL=ROCK_LAENGE_CM,
        v_abnaeher=1.5, h_abnaeher_2=2.5,
    )
    sag(f"Rock S.33  HueW {t_rk.HueW}  TaW {t_rk.TaW}  TaAf {t_rk.TaAf}  "
        f"Kontrolle {t_rk.kontrolle_taillenausfall()}")
    gr = gerader_rock(t_rk)
    for h in gr.hinweise:
        sag(f"       ! {h}")
    rk = saumerweitert(gr, saumerweiterung_cm=SAUMERWEITERUNG_CM)
    sag(f"Rock S.43  Oeffnungsbetrag {rk.oeffnungsbetrag_cm:.1f} cm je Keil "
        f"(6 Keile)  Saumweite {rk.saumweite_cm} cm")
    sag(f"           verbleibender RT-Abnaeher {rk.rest_abnaeher_cm:.1f} cm")
    for h in rk.hinweise:
        sag(f"       ! {h}")

    # ------------------------------------------------ Kontrolle Taillennaht
    ot_taille = (
        polylinie_laenge(ot.vt_teil["taille_basis"]) - cm(ot.vAbl_cm)
        + polylinie_laenge(ot.rt_teil["taille_basis"]) - cm(ot.shAbl_cm) - cm(ot.hAbl_cm)
    )
    rk_taille = cm(rk.taillenweite_cm) / 2.0
    sag()
    sag("Kontrolle Taillennaht (halber Schnitt):")
    sag(f"  Oberteil {mm_zu_cm(ot_taille):.2f} cm   Rock {mm_zu_cm(rk_taille):.2f} cm   "
        f"Differenz {mm_zu_cm(ot_taille - rk_taille):+.2f} cm")
    if abs(ot_taille - rk_taille) > cm(0.5):
        sag("  ! Ueber 0,5 cm Differenz. Vor dem Zuschnitt ausgleichen "
            "(Zugabe TaU oder Abnaeherinhalte anpassen).")

    # ==================================================== Schnittteile bauen
    teile: list[Schnittteil] = []
    y_brust = gg.y_brustlinie
    y_taille = gg.y_taillenlinie
    x_vm = gg.x_vm
    x_hm_taille = gg.punkt["P7"][0]

    # --- Rueckteile: tiefer V-Ausschnitt, hM als Naht mit Verschluss --------
    v_spitze = (x_hm_taille, y_taille - cm(RUECKEN_V_UEBER_TAILLE_CM))
    rt_seite_brust = gg.punkt["P11"]

    rt_rechts = Schnittteil(
        "RT rechts 1x - mit Schulterband",
        _behalte_mit(ot.rt_kontur, gg.punkt["HlP_h"], v_spitze,
                     referenz=gg.punkt["P11"]),
    )
    rt_links = Schnittteil(
        "RT links 1x - ohne Schulter",
        _behalte_mit(ot.rt_kontur, rt_seite_brust, v_spitze,
                     referenz=(x_hm_taille, y_taille)),
    )
    schnitte = {
        "RT rechts 1x": (gg.punkt["HlP_h"], v_spitze, gg.punkt["P11"]),
        "RT links 1x": (rt_seite_brust, v_spitze, (x_hm_taille, y_taille)),
    }
    for teil, txt in ((rt_rechts, "RT rechts 1x"), (rt_links, "RT links 1x")):
        a, b, ref = schnitte[txt]
        for ab in ot.abnaeher:
            if ab.name not in ("hAbl", "shAbl", "Schulterabnaeher"):
                continue
            if not _innerhalb([ab.schenkel_a, ab.schenkel_b], a, b, ref):
                continue
            ab2, meldung = _gekuerzt(ab, a, b, ref)
            if meldung:
                sag(f"       ! {txt}: {meldung}")
            if ab2 is None:
                continue
            for l in ab2.linien():
                teil.hilfslinie(l, "ABNAEHER")
        teil.hilfslinie([(x_hm_taille, y_taille), (x_hm_taille, y_taille - cm(20))],
                        "SCHLITZ")
        _fadenlauf(teil, x_hm_taille - cm(6), y_taille - cm(28), y_taille - cm(6))
        teil.beschrifte(txt, (x_hm_taille - cm(14), y_taille - cm(16)), 9.0)
        teil.beschrifte("hM = Naht + Verschluss",
                        (x_hm_taille - cm(9), y_taille - cm(19)), 6.0)
        teile.append(teil)

    # --- Vorderteile -------------------------------------------------------
    vt_halb = ot.vt_kontur
    vt_seitennaht_bei = lambda y: schnitt_mit_waagerechter(
        gg.punkt["P12"], ot.vt_teil["seitennaht"][-1], y)

    # Untertritt: linke Haelfte, gerade Oberkante
    p_seite_u = vt_seitennaht_bei(y_brust + cm(UNTERTRITT_SEITE_CM))
    p_vm_u = (x_vm, y_brust + cm(UNTERTRITT_VM_CM))
    untertritt = Schnittteil(
        "lVT Untertritt 1x",
        _behalte_mit(vt_halb, p_vm_u, p_seite_u, referenz=(x_vm, y_taille)),
    )

    # Wickelteil: ganzes Vorderteil, ein Schulterband rechts
    vt_ohne_vm = vt_halb[1:]
    vt_ganz = vt_ohne_vm + [spiegle_senkrecht(p, x_vm) for p in reversed(vt_ohne_vm)]
    p_seite_w = spiegle_senkrecht(
        vt_seitennaht_bei(y_brust + cm(WICKELKANTE_SEITE_CM)), x_vm)
    wickel = Schnittteil(
        "rVT Wickelteil 1x",
        _behalte_mit(vt_ganz, gg.punkt["HlP_v"], p_seite_w,
                     referenz=(x_vm, y_taille)),
    )

    for teil, txt, gespiegelt in ((untertritt, "lVT Untertritt 1x", False),
                                  (wickel, "rVT Wickelteil 1x", True)):
        for ab in ot.abnaeher:
            if ab.name == "vAbl":
                for l in ab.linien():
                    teil.hilfslinie(l, "ABNAEHER")
                if gespiegelt:
                    for l in ab.linien():
                        teil.hilfslinie(spiegle_alle(l, x_vm), "ABNAEHER")
        # Brustabnaeher-Linie und BrP als Konstruktionslinie (S.181 Schritt 22)
        brp = gg.punkt["BrP"]
        teil.hilfslinie([(brp[0], brp[1] - cm(9)), (brp[0], brp[1] + cm(9))],
                        "HILFSLINIE")
        teil.hilfslinie([(brp[0] - cm(1), brp[1]), (brp[0] + cm(1), brp[1])],
                        "HILFSLINIE")
        if gespiegelt:
            b2 = spiegle_senkrecht(brp, x_vm)
            teil.hilfslinie([(b2[0], b2[1] - cm(9)), (b2[0], b2[1] + cm(9))],
                            "HILFSLINIE")
            teil.hilfslinie([(b2[0] - cm(1), b2[1]), (b2[0] + cm(1), b2[1])],
                            "HILFSLINIE")
        _fadenlauf(teil, x_vm, y_taille - cm(24), y_taille - cm(4))
        teil.beschrifte(txt, (x_vm + cm(2), y_taille - cm(12)), 9.0)
        teil.beschrifte(f"BrP - Brustabnaeher {ot.brustabnaeher_grad:.1f} Grad offen",
                        (x_vm + cm(2), y_taille - cm(9)), 5.0)
        teil.beschrifte("S.184 Schritt 26/27 am Buch pruefen",
                        (x_vm + cm(2), y_taille - cm(7)), 5.0)
        teile.append(teil)

    # --- Rockteile ---------------------------------------------------------
    rock_vt = Schnittteil("Rock VT 2x", rk.vt_kontur)
    rock_vt.hilfslinie([(0.0, gr.y_saumlinie),
                        (0.0, gr.y_saumlinie - cm(SCHLITZ_HOEHE_CM))], "SCHLITZ")
    rock_vt.beschrifte(f"Schlitz {SCHLITZ_HOEHE_CM:.0f} cm ab Saum",
                       (cm(1), gr.y_saumlinie - cm(SCHLITZ_HOEHE_CM / 2)), 7.0)
    rock_vt.beschrifte("Rock VT 2x - vM = Naht", (cm(4), cm(30)), 9.0)
    _fadenlauf(rock_vt, cm(6), cm(20), cm(70))
    teile.append(rock_vt)

    rock_rt = Schnittteil("Rock RT 2x", rk.rt_kontur)
    if rk.rt_abnaeher:
        for l in rk.rt_abnaeher.linien():
            rock_rt.hilfslinie(l, "ABNAEHER")
    rock_rt.hilfslinie([(gr.x_hm, 0.0), (gr.x_hm, cm(20))], "SCHLITZ")
    rock_rt.beschrifte("Rock RT 2x - hM = Naht + Reiszverschluss",
                       (gr.x_hm - cm(30), cm(30)), 9.0)
    _fadenlauf(rock_rt, gr.x_hm - cm(6), cm(20), cm(70))
    teile.append(rock_rt)

    pfad = schreibe_dxf(teile, ziel)
    sag()
    sag(f"DXF geschrieben: {pfad}")
    sag(f"  {len(teile)} Schnittteile, Einheit Millimeter, ohne Nahtzugaben")
    (ziel.parent / "protokoll.txt").write_text("\n".join(protokoll) + "\n",
                                               encoding="utf-8")


if __name__ == "__main__":
    bauen(Path(__file__).resolve().parent / "ausgabe" / "kleid_lumiere_gr38.dxf")

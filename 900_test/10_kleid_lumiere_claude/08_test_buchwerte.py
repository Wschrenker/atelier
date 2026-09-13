"""Pruefwerte aus dem Buch.

Regel aus `500_python/AGENT.md`: **ohne Pruefwert kein Modul.** Jeder Test hier
nennt seine Buchseite. Wo das Buch keine Beispielzahl druckt, steht das
ausdruecklich dabei; solche Werte sind Regressionswerte und **nicht aus dem
Buch**.

Aufruf:

    python -m pytest 500_python/10_rechnung/test_buchwerte.py
    python 500_python/10_rechnung/test_buchwerte.py     # ohne pytest
"""

from __future__ import annotations

import sys
from dataclasses import replace
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from masse import koerpermasse
from oberteil import konstruktionstabelle, grundgeruest, tailliert
from rock import konstruktionstabelle_rock, gerader_rock, saumerweitert, vollglocke


def nah(a: float, b: float, toleranz: float = 0.05) -> bool:
    return abs(a - b) <= toleranz


# --------------------------------------------------------------------- S.20

def test_groessentabelle_s20():
    """S.20, Spalte Groesze 38."""
    m = koerpermasse(38)
    assert (m.BrU, m.TaU, m.HueU) == (88, 72, 97)
    assert (m.HlB, m.AlT, m.RueL, m.HueT) == (6.5, 20.1, 41.6, 21)
    assert (m.BrT, m.VL, m.RueB, m.ArD, m.BrB) == (28.1, 45.3, 16.5, 9.3, 18.2)
    assert (m.SuB, m.SuWi, m.sTaH) == (12.2, 20, 106)
    # S.177 nennt die individuelle Balance des Beispiels mit 3,7
    assert nah(m.balance(), 3.7, 0.001)


# --------------------------------------------------------------------- S.44

def test_vollglocke_s44():
    """S.44, Berechnungsbeispiel: TaW 72, MoL 50, pi = 3,14."""
    g = vollglocke(72, 50, pi=3.14)
    assert nah(g.rTaW_cm, 11.5, 0.05)     # Buch: 11,5
    assert nah(g.rSaW_cm, 61.5, 0.05)     # Buch: 61,5
    # Das Buch rechnet die Saumweite aus dem gerundeten Radius: 2 x 3,14 x 61,5
    assert nah(2 * 3.14 * round(g.rSaW_cm, 1), 386.2, 0.05)


def test_vollglocke_s44_nahtzugabe():
    """S.44, Radiusformel bei Naht-/Schlitzloesung. Buch nennt keinen NZg-Wert."""
    ohne = vollglocke(72, 50, pi=3.14)
    mit = vollglocke(72, 50, NZg_cm=1.0, pi=3.14)
    assert nah(mit.rTaW_cm - ohne.rTaW_cm, 2.0 / (2 * 3.14), 0.001)


# ------------------------------------------------------------- S.177 / S.178

def test_konstruktionstabelle_s177():
    """S.177: taillierter Oberteil-GS, Groesze 38, PK 4."""
    t = konstruktionstabelle(koerpermasse(38))
    assert (t.BrW, t.halb_BrW) == (96, 48)
    assert (t.TaW, t.halb_TaW) == (78, 39)
    assert (t.HueW, t.halb_HueW) == (101, 50.5)
    assert nah(t.AlT_plus, 21.8, 0.001)
    assert nah(t.RueB_plus, 17.3, 0.001)
    assert nah(t.ArD_plus, 11.3, 0.001)
    assert nah(t.BrB_plus, 19.4, 0.001)
    assert nah(t.SuNL, 12.6, 0.001)
    assert nah(t.hSuNL, 13.3, 0.001)
    # Kontrolle des Buchs: RueB+ + ArD+ + BrB+ = 1/2 BrW
    assert nah(t.kontrolle_brustweite(), 0.0, 1e-9)


def test_buchfehler_s178_wird_nicht_uebernommen():
    """S.178, PK 3: zwei Rechenwidersprueche, im Transkript markiert.

    Das Buch druckt `AlT+ = 21,8` (20,1 + 1,3 ergibt 21,4) und `1/2 BrW = 48`
    (94 : 2 ergibt 47). S.186 druckt fuer AlT+ den richtigen Wert 21,4.
    Der Code rechnet richtig und uebernimmt den Druckfehler **nicht**.
    """
    t = konstruktionstabelle(
        koerpermasse(38), passformklasse=3,
        zg_BrU=6.0, zg_TaU=4.0, zg_HueU=4.0, zg_AlT=1.3,
        zg_RueB=0.5, zg_ArD=1.5, zg_BrB=1.0, zg_SuB=0.3,
    )
    assert nah(t.AlT_plus, 21.4, 0.001)   # nicht 21,8
    assert nah(t.halb_BrW, 47.0, 0.001)   # nicht 48
    assert nah(t.kontrolle_brustweite(), 0.0, 1e-9)


# ------------------------------------------------------------- S.184 / S.185

def _tabelle_pk3():
    """Konstruktionstabelle des Buchbeispiels S.178.

    S.178 vermerkt ausdruecklich: "Der TaU ist hier um 4 cm kleiner als in der
    Groeszentabelle fuer die Groesze 38." Das Beispiel rechnet also mit einem
    gemessenen TaU von 68 statt der Tabellengroesze 72.
    """
    return konstruktionstabelle(
        replace(koerpermasse(38), TaU=68.0), passformklasse=3,
        zg_BrU=6.0, zg_TaU=4.0, zg_HueU=4.0, zg_AlT=1.3,
        zg_RueB=0.5, zg_ArD=1.5, zg_BrB=1.0, zg_SuB=0.3,
    )


def test_taillenausfall_s184_s185():
    """S.184 Schritte 36 und 38, S.185 Abschnitt 12 - Buchbeispiel PK 3.

    Buchwerte: me 2,2 · vAbl 3,2 · TaB 42,8 · 1/2 TaW 36 · TaAf 6,8
    """
    t = _tabelle_pk3()
    assert (t.TaU, t.TaW, t.halb_TaW) == (68.0, 72.0, 36.0)
    ot = tailliert(grundgeruest(t))
    assert nah(ot.me_cm, 2.2, 0.05)
    assert nah(ot.vAbl_cm, 3.2, 0.05)
    assert nah(ot.vTaB_cm + ot.hTaB_cm, 42.8, 0.1)
    assert nah(ot.TaAf_cm, 6.8, 0.1)


def test_aufteilung_taillenausfall_s185():
    """S.185 Abschnitt 12: SN 2,0 + shAbl 2,0 + hAbl 2,8 = TaAf 6,8."""
    ot = tailliert(grundgeruest(_tabelle_pk3()))
    assert nah(ot.sn_cm + ot.shAbl_cm + ot.hAbl_cm, ot.TaAf_cm, 1e-6)
    assert nah(ot.shAbl_cm, 2.0, 0.15)
    assert nah(ot.hAbl_cm, 2.8, 0.15)


def test_kontur_geschlossen():
    """Invariante, nicht aus dem Buch: die Konturen sind endlich und geschlossen."""
    ot = tailliert(grundgeruest(konstruktionstabelle(koerpermasse(38))))
    for kontur in (ot.vt_kontur, ot.rt_kontur):
        assert len(kontur) > 20
        assert all(all(map(lambda v: v == v and abs(v) < 1e6, p)) for p in kontur)


# --------------------------------------------------------------- S.33 / S.35

def test_konstruktionstabelle_rock_s33():
    """S.33: gerader Rock, Groesze 38, HueU 97 + 3, TaU 72 + 2."""
    t = konstruktionstabelle_rock(koerpermasse(38))
    assert (t.HueW, t.halb_HueW) == (100, 50)
    assert (t.TaW, t.halb_TaW) == (74, 37)
    assert nah(t.TaAf, 13.0, 1e-9)
    assert nah(t.hueftabstich, 6.5, 1e-9)
    assert nah(t.v_abnaeher, 2.5, 1e-9)
    assert nah(t.h_abnaeher_1, 4.0, 1e-9)      # Buch: Rest = 4,0
    assert nah(t.kontrolle_taillenausfall(), 0.0, 1e-9)


def test_rock_zwei_rt_abnaeher_s35():
    """S.35: Variante mit zwei RT-Abnaehern - 6 + 1,5 + 3 + 2,5 = 13."""
    t = konstruktionstabelle_rock(
        koerpermasse(38), hueftabstich=6.0, v_abnaeher=1.5, h_abnaeher_2=2.5)
    assert nah(t.h_abnaeher_1, 3.0, 1e-9)
    assert nah(t.kontrolle_taillenausfall(), 0.0, 1e-9)


# --------------------------------------------------------------------- S.43

def test_oeffnungsbetrag_s43():
    """S.43: Oeffnungsbetrag = Saumerweiterung : 6. Buchbeispiel 48 : 6 = 8."""
    gr = gerader_rock(konstruktionstabelle_rock(koerpermasse(38)))
    se = saumerweitert(gr, saumerweiterung_cm=48.0)
    assert nah(se.oeffnungsbetrag_cm, 8.0, 1e-9)


def test_saumweite_waechst_um_die_erweiterung():
    """Invariante, nicht aus dem Buch.

    Der gerade Rock-GS hat Saumweite = HueW (S.32: "Hueft- und Saumweite sind
    also gleich"). Nach der Erweiterung musz die Saumweite um genau die
    gewuenschte Erweiterung groeszer sein.
    """
    t = konstruktionstabelle_rock(koerpermasse(38))
    se = saumerweitert(gerader_rock(t), saumerweiterung_cm=48.0)
    assert nah(se.saumweite_cm, t.HueW + 48.0, 1.0)


if __name__ == "__main__":
    fehler = 0
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            try:
                fn()
                print(f"  ok    {name}")
            except AssertionError as exc:
                fehler += 1
                print(f"  FEHLT {name}  {exc}")
    print(f"\n{fehler} Fehler")
    sys.exit(1 if fehler else 0)

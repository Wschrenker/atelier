"""S.-35-Arbeitskontur, explizit eigene Kurvenwahl und kein Produktionsschnitt.

Nur achsenparallele lokale Teile: Mitte links, Seitennaht rechts, Y nach unten.
Das Beispiel montiert bestehende S.-33/34/35-Funktionen, nicht kopierte Formeln.
"""
from dataclasses import dataclass
from importlib.util import spec_from_file_location, module_from_spec
from pathlib import Path
import sys
import math

from kurven import Punkt, Kubisch, KurvenVertragError, taillenbogen, hueftbogen, messen


@dataclass(frozen=True)
class Abnaeher:
    links: Punkt
    rechts: Punkt
    spitze: Punkt
    inhalt_mm: float


@dataclass(frozen=True)
class Teilbasis:
    name: str
    mitte: Punkt
    seite_oben: Punkt
    breite_mm: float
    huefttiefe_mm: float
    laenge_mm: float
    abnaeher: tuple[Abnaeher, ...]


@dataclass(frozen=True)
class Arbeitskontur:
    taille: tuple[tuple[Kubisch, ...], ...]
    huefte: Kubisch
    ring: tuple[Punkt, ...]  # Explizit geschlossen; Mundkanten bleiben im Papier.
    taillenlaenge_mm: tuple[float, float]  # Ohne Abnähermund; NICHT virtuell genäht.
    seitenlaenge_mm: tuple[float, float]
    status: str = 'arbeitskontur_nicht_produktionsfreigegeben'


def _laden(name, relativ):
    """Bestehendes Modul per festem Kapitelpfad; kein Import aus Fremdbeständen."""
    modulname = '_s35_arbeitskontur_' + name
    if modulname not in sys.modules:
        pfad = Path(__file__).resolve().parents[2] / relativ
        spec = spec_from_file_location(modulname,pfad)
        modul = module_from_spec(spec)
        sys.modules[modulname] = modul
        spec.loader.exec_module(modul)
    return sys.modules[modulname]


def arbeitsbeispiel() -> dict[str, Teilbasis]:
    """Neutrales, buchnahes Prüfbeispiel; KEIN Kundinnenprofil.

    Gewählt: halbe Hüftweite 500, Länge 500, Hüfttiefe 200, TaU 740 mm;
    seitliche Erhöhung 10, vordere 5 mm; Abnäherlängen 90/145/130 mm.
    S.-35-Verteilung: Hüftabstich 60, VT 15, RT 30+25 mm.
    Nicht alle diese Entscheidungen sind ein zusammengehöriger Buchdatensatz.
    """
    g = _laden('geruest', '01_gerader_rock_konstruktionstabelle_und_grundgeruest_s32-33/02_grundgeruest_zeichnen_s33/grundgeruest.py')
    e = _laden('erhoehung', '02_abnaeher_positionieren_s34/01_taillenlinien_erhoehen_s34/taillenlinien_erhoehen.py')
    h = _laden('hueftpunkte', '02_abnaeher_positionieren_s34/03_hueftbogen_und_abnaeher_zeichnen_s34/hueftbogen_und_abnaeher.py')
    r = _laden('rueckteil', '03_rueckteil_mit_zwei_abnaehern_s35/01_zwei_hintere_abnaeher_konstruieren_s35/zwei_hintere_abnaeher.py')
    geruest = g.grundgeruest_zeichnen(modelllaenge_mm=500,huefttiefe_mm=200,halbe_hueftweite_mm=500)
    erhoeht = e.taillenlinien_erhoehen(p7=geruest.p7,p8=geruest.p8,
        taillenlinie_start=geruest.p1,taillenlinie_ende=geruest.p4,
        taillenerhoehung_seitenlinie_mm=10,taillenerhoehung_vorderer_abnaeher_mm=5)
    punkte = h.hueftbogen_und_abnaeher_konstruieren(
        vordere_mitte=geruest.p1,p7=geruest.p7,p8=geruest.p8,hintere_mitte=geruest.p4,
        taillenerhoehung_seitenlinie_mm=erhoeht.taillenerhoehung_seitenlinie_mm,
        taillenerhoehung_vorderer_abnaeher_mm=erhoeht.taillenerhoehung_vorderer_abnaeher_mm,
        taillenerhoehung_hinterer_abnaeher_mm=erhoeht.taillenerhoehung_hinterer_abnaeher_mm,
        hueftabstich_mm=60,taillenumfang_mm=740,vorderer_abnaeherinhalt_mm=15,
        hinterer_abnaeherinhalt_mm=0,vordere_abnaeherlaenge_mm=90,hintere_abnaeherlaenge_mm=None)
    hinten = r.zwei_hintere_abnaeher_konstruieren(p7=geruest.p7,p8=geruest.p8,
        hintere_mitte=geruest.p4,hinterer_hueftbogenpunkt=punkte.hinterer_hueftbogenpunkt,
        taillenausfall_mm=130,hueftabstich_mm=60,vorderer_abnaeherinhalt_mm=15,
        hinterer_gesamtinhalt_mm=55,inhaltsdifferenz_mm=5,positionskorrektur_erster_abnaeher_mm=0,
        taillenerhoehung_seitenlinie_mm=erhoeht.taillenerhoehung_seitenlinie_mm,
        taillenerhoehung_vorderer_abnaeher_mm=erhoeht.taillenerhoehung_vorderer_abnaeher_mm,
        taillenerhoehung_erster_hinterer_abnaeher_mm=erhoeht.taillenerhoehung_hinterer_abnaeher_mm,
        laenge_erster_hinterer_abnaeher_mm=145,laenge_zweiter_hinterer_abnaeher_mm=130)
    def vt(p):
        return Punkt(p.x_mm,p.y_mm)
    def rt(p):
        return Punkt(geruest.p4.x_mm-p.x_mm,p.y_mm)
    v = punkte.vorderer_abnaeher
    ra = tuple(Abnaeher(rt(a.schenkel_zur_hinteren_mitte),rt(a.schenkel_zur_seitennaht),
                       rt(a.spitze),a.inhalt_mm)
               for a in (hinten.erster_abnaeher,hinten.zweiter_abnaeher))
    return {
        'VT': Teilbasis('VT',vt(geruest.p1),vt(punkte.vorderer_hueftbogenpunkt),
                        geruest.p9.x_mm,geruest.p9.y_mm,geruest.p2.y_mm,
                        (Abnaeher(vt(v.schenkel_vorne),vt(v.schenkel_hinten),vt(v.spitze),v.inhalt_mm),)),
        'RT': Teilbasis('RT',rt(geruest.p4),rt(punkte.hinterer_hueftbogenpunkt),
                        geruest.p4.x_mm-geruest.p9.x_mm,geruest.p9.y_mm,geruest.p5.y_mm,ra),
    }


def kontur(basis: Teilbasis, *, durchhang_mm: float, hueftform: float) -> Arbeitskontur:
    """Arbeits-Papierkontur; ungeformte Abnäher innen, noch kein Abnäherdach."""
    punkte = [basis.mitte,basis.seite_oben]
    werte = [basis.breite_mm,basis.huefttiefe_mm,basis.laenge_mm,durchhang_mm,hueftform]
    for a in basis.abnaeher:
        punkte.extend((a.links,a.rechts,a.spitze))
        werte.append(a.inhalt_mm)
    werte.extend(w for p in punkte for w in (p.x_mm,p.y_mm))
    if not all(math.isfinite(w) for w in werte):
        raise KurvenVertragError('Teilbasis und Parameter müssen endlich sein')
    if not (basis.mitte == Punkt(0,0) and
            0 < basis.seite_oben.x_mm <= basis.breite_mm and
            basis.seite_oben.y_mm <= 0 < basis.huefttiefe_mm < basis.laenge_mm):
        raise KurvenVertragError('Nur lokale aufrechte Teile: Mitte (0,0), Hüfte vor Saum')
    letzte_x = 0
    for a in basis.abnaeher:
        if not (letzte_x < a.links.x_mm < a.spitze.x_mm < a.rechts.x_mm < basis.seite_oben.x_mm
                and a.links.y_mm == a.rechts.y_mm < a.spitze.y_mm < basis.huefttiefe_mm
                and a.inhalt_mm > 0
                and math.isclose(a.rechts.x_mm-a.links.x_mm,a.inhalt_mm,abs_tol=1e-9,rel_tol=0)):
            raise KurvenVertragError('Abnäherlage, Mundweite oder Reihenfolge ungültig')
        letzte_x = a.rechts.x_mm
    tiefengrenze = min([basis.huefttiefe_mm]+[a.spitze.y_mm for a in basis.abnaeher])
    abschnitte = []
    ring = [basis.mitte]
    start = basis.mitte
    unten = oben = 0.0
    for ab in (*basis.abnaeher, None):
        ende = ab.links if ab else basis.seite_oben
        kurven = taillenbogen(start,ende,durchhang_mm=durchhang_mm)
        abschnitte.append(kurven)
        for k in kurven:
            if max(p.y_mm for p in (k.p0,k.p1,k.p2,k.p3)) >= tiefengrenze:
                raise KurvenVertragError('Arbeitskurve erreicht Hüftlinie oder Abnäherspitzenhöhe')
            m = messen(k,fehler_mm=0.001)
            ring.extend(m.punkte[1:])
            unten += m.untergrenze_mm
            oben += m.obergrenze_mm
        if ab:
            ring.append(ab.rechts)
            start = ab.rechts
    h = hueftbogen(basis.seite_oben,Punkt(basis.breite_mm,basis.huefttiefe_mm),form=hueftform)
    m = messen(h,fehler_mm=0.001)
    ring.extend(m.punkte[1:])
    ring.extend((Punkt(basis.breite_mm,basis.laenge_mm),Punkt(0,basis.laenge_mm),basis.mitte))
    rest = basis.laenge_mm-basis.huefttiefe_mm
    return Arbeitskontur(tuple(abschnitte),h,tuple(ring),(unten,oben),
                         (m.untergrenze_mm+rest,m.obergrenze_mm+rest))

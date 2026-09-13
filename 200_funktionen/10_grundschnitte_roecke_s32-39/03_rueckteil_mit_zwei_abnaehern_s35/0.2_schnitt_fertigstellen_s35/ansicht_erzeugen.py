"""Lokale Offline-Ansicht aus Python-Kurven; JavaScript zeichnet nur gelieferte Pfade."""
from dataclasses import asdict
import json
from pathlib import Path
from grundkontur import arbeitsbeispiel, kontur


def _xy(p):
    return f'{p.x_mm:.12g},{p.y_mm:.12g}'


def _c(k):
    return 'C'+ ' '.join(_xy(p) for p in (k.p1,k.p2,k.p3))


def ansichtsdaten():
    """Diskrete Reglerstellungen; Grenzen sind UI-Erkundungswahl, keine Buchregel."""
    durchhang = [i/4 for i in range(13)]
    form = [(4+i)/40 for i in range(17)]
    daten = dict(status='arbeitskontur_nicht_produktionsfreigegeben',
                 durchhang_mm=durchhang,hueftform=form,teile={})
    for name,b in arbeitsbeispiel().items():
        taillen, hueften = [], []
        for s in durchhang:
            k = kontur(b,durchhang_mm=s,hueftform=0.3)
            voll = 'M'+_xy(b.mitte)
            naht = ''
            for i,gruppe in enumerate(k.taille):
                befehle = ''.join(_c(c) for c in gruppe)
                voll += befehle
                naht += 'M'+_xy(gruppe[0].p0)+befehle
                if i < len(b.abnaeher):
                    voll += 'L'+_xy(b.abnaeher[i].rechts)
            taillen.append(dict(kontur=voll,naht=naht,laenge_mm=list(k.taillenlaenge_mm)))
        for f in form:
            k = kontur(b,durchhang_mm=1,hueftform=f)
            hueften.append(dict(kontur=_c(k.huefte),
                                naht='M'+_xy(b.seite_oben)+_c(k.huefte)+f'L{b.breite_mm},{b.laenge_mm}',
                                laenge_mm=list(k.seitenlaenge_mm)))
        abnaeher = ''.join('M'+_xy(a.links)+'L'+_xy(a.spitze)+'L'+_xy(a.rechts)
                          for a in b.abnaeher)
        muender = ''.join('M'+_xy(a.links)+'L'+_xy(a.rechts) for a in b.abnaeher)
        anker = [b.mitte,b.seite_oben]+[p for a in b.abnaeher for p in (a.links,a.rechts,a.spitze)]
        daten['teile'][name] = dict(basis=asdict(b),taillen=taillen,hueften=hueften,
            abnaeher=abnaeher,muender=muender,anker=[asdict(p) for p in anker],
            schluss=f'L{b.breite_mm},{b.laenge_mm}L0,{b.laenge_mm}Z')
    return daten


def html_erzeugen() -> str:
    vorlage = Path(__file__).with_name('kurvenansicht.vorlage.html').read_text(encoding='utf-8')
    return vorlage.replace('__KURVENDATEN__',json.dumps(ansichtsdaten(),ensure_ascii=False,allow_nan=False))


if __name__ == '__main__':
    ziel = Path(__file__).with_name('kurvenansicht.html')
    # Dieser Dateiname gehört ausschließlich diesem reproduzierbaren Generator.
    ziel.write_text(html_erzeugen(),encoding='utf-8')
    print(f'Erzeugt: {ziel} ({ziel.stat().st_size} Bytes)')

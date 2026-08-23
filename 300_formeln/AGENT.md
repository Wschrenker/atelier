# Formeln — was hier drin gilt

## Navigation — Regel

Diese Datei führt nur zu den direkten Unterordnern von `300_formeln/`.
Fachdateien werden ausschließlich im zuständigen unteren `AGENT.md` geführt.

## Navigation

- [ ] `10_masse/AGENT.md`
- [ ] `20_rock/AGENT.md`
- [ ] `30_oberteil/AGENT.md`
- [ ] `40_hose/AGENT.md`
- [ ] `50_aermel/AGENT.md`
- [ ] `60_kragen_kapuze/AGENT.md`
- [ ] `70_details_verarbeitung/AGENT.md`

## Aktueller Stand

Der Formelbereich ist bewusst **leer**. Zuerst werden die Buchtranskripte gegen
das Original geprüft, danach Abkürzungen und Gosslar-Begriffe belegt. Erst dann
werden Formeln seitenweise eingepflegt.

## Zweck

Hier stehen verifizierte Maßregister und Konstruktionsformeln in lesbarer
Rechenform, noch nicht als Python-Code.

## Eingangssperre

Eine Formel darf erst hierher, wenn:

1. die Buchseite in `100_quellen` am Original freigegeben ist,
2. alle formelrelevanten Prüfstellen aufgelöst oder ausdrücklich als
   Buchwiderspruch markiert sind,
3. verwendete Abkürzungen in `000_sprache` belegt sind,
4. Buchseite und genauer Transkriptpfad feststehen,
5. der Buchprüfwert nachgerechnet wurde oder ausdrücklich keiner vorhanden ist.

Das Buchbild bestätigt das Transkript. Das Transkript bestätigt Sprache und
Formel — niemals umgekehrt.

## Grenze

| Nicht hier | Sondern |
|---|---|
| Buchbilder und Transkripte | `100_quellen/` |
| Abkürzungen und Begriffe | `000_sprache/` |
| Geometrie-Primitive | `400_mathematik/` |
| Python und Tests | `500_python/` |
| Arbeitslisten | `600_prozess/` |

Es gibt keine Quellenkopien in diesem Ordner. Die maßgeblichen Transkripte
bleiben unter `100_quellen`.

## Form eines Formelblocks

Jeder Formelblock trägt mindestens:

- stabile Kennung `F-<seite>-<laufende Nummer>`,
- Originalwortlaut und mathematische Lesart getrennt,
- Eingänge, Ergebnis und Einheiten,
- genaue Buchseite und Transkriptpfad,
- Buchprüfwert oder „keiner im Buch“,
- Rechenprüfung und Freigabestatus,
- offene Widersprüche sichtbar als `⚠️`.

## Fertig-Regel

Nur eine fachlich nachvollziehbare und freigegebene Formel darf von
`500_python` verwendet werden. Ohne verifizierte Quelle, geklärte Abkürzungen
und nachgerechneten Prüfwert beginnt kein Python-Modul.

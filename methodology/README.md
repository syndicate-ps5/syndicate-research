# Methodik

## Zweck

Dieser Ordner legt fest, wie Sachaussagen in das öffentliche Repository aufgenommen werden. Er enthält die Bewertungsregeln, keine Forschungsergebnisse.

## Aufnahmeregel

Aufgenommen werden nur verifizierte Inhalte mit Quellenangabe. Interne oder unverifizierte Daten gehören ausschließlich in das private Repository `syndicate-lab`.

## Evidenzstufen

| Stufe | Bedeutung |
| --- | --- |
| Publicly Documented | Eine öffentliche Primärquelle belegt die Aussage. |
| Independently Reproduced | Die Aussage wurde außerhalb der Originalquelle nachvollzogen. |
| Internally Tested | Ein interner Test liegt vor. Das allein reicht für dieses Repository nicht. |
| Unverified | Die Aussage ist nicht geprüft. |
| Unknown | Für die Frage gibt es keinen Beleg. |

Publicly Documented und Independently Reproduced können hier erscheinen, wenn der Owner die Veröffentlichung freigibt und die Quelle am Eintrag steht. Internally Tested bleibt in `syndicate-lab`, bis diese Freigabe vorliegt. Unverified wird hier nicht als Ergebnis geführt. Unknown wird ausdrücklich gekennzeichnet.

## Aufgabenstatus

Die Status Planned, In Progress, Implemented, Tested, Verified und Blocked sind in der [README](../README.md) definiert.

**Implemented bedeutet nicht automatisch Verified.**

Ein Dokument kann Implemented sein, sobald es im Repository steht, und bleibt so lange auf diesem Status, bis die Quellenprüfung abgeschlossen ist. Verified setzt diese Prüfung voraus. Bei Publicly Documented ist die Prüfung der Abgleich mit der Primärquelle. Bei Independently Reproduced ist es der dokumentierte Nachvollzug.

## Arbeitsregeln

- Jede wichtige Aussage hat eine Quelle und ein Abrufdatum.
- Der übernommene Sachumfang wird benannt. Darüber hinaus wird nichts ergänzt.
- Hardware und Firmware werden getrennt dokumentiert.
- Kompatibilität wird nicht aus der Modellgruppe abgeleitet.
- Geheimnisse, Exploit-Beschreibungen und unveröffentlichte Schwachstellen werden nicht aufgenommen. Meldungen folgen [`SECURITY.md`](../SECURITY.md).

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
| Unknown | Die geprüften Quellen belegen die Aussage nicht. |
| Researching | Die Frage ist offen. Die Quellenprüfung ist nicht abgeschlossen. |

Publicly Documented und Independently Reproduced können hier erscheinen, wenn die Quelle am Eintrag steht. Internally Tested bleibt in `syndicate-lab`, bis der Owner die Veröffentlichung freigibt. Unverified wird hier nicht als Ergebnis geführt. Unknown und Researching werden an der offenen Frage ausgeschrieben. Researching ist kein Beleg und berechtigt nicht, eine Vermutung einzutragen.

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

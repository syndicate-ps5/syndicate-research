# Glossar

## Zweck

Dieser Ordner definiert die Arbeitsbegriffe des öffentlichen Repositories. Fachbegriffe zu Hardware oder Firmware werden hier erst aufgenommen, wenn sie an einer verifizierten Stelle verwendet werden und eine Quelle haben.

## Aufnahmeregel

Aufgenommen werden nur verifizierte Inhalte mit Quellenangabe. Interne oder unverifizierte Daten gehören ausschließlich in das private Repository `syndicate-lab`.

## Aufgabenstatus

| Begriff | Bedeutung |
| --- | --- |
| Planned | Vorgesehen, noch nicht begonnen |
| In Progress | In Arbeit |
| Implemented | Umgesetzt, aber noch nicht als verifiziert abgeschlossen |
| Tested | Ein nachvollziehbarer Test wurde ausgeführt |
| Verified | Ergebnis wurde gegen die festgelegte Grundlage bestätigt |
| Blocked | Durch eine offene Abhängigkeit aufgehalten |

Implemented bedeutet nicht automatisch Verified.

## Evidenzstufen

| Begriff | Bedeutung |
| --- | --- |
| Publicly Documented | Durch eine öffentliche Primärquelle belegt |
| Independently Reproduced | Außerhalb der Originalquelle nachvollzogen |
| Internally Tested | Intern geprüft; allein noch nicht veröffentlichungsreif |
| Unverified | Nicht geprüft |
| Unknown | In den geprüften Quellen nicht belegt |
| Researching | Quellenprüfung nicht abgeschlossen; keine Sachaussage |

Die Anwendung dieser Stufen steht in [`methodology/README.md`](../methodology/README.md).

## Weitere Begriffe

| Begriff | Bedeutung |
| --- | --- |
| Modellgruppe | Von Sony in einer Primärquelle verwendete Gruppenbezeichnung. Die hier geführten Gruppen sind CFI-1000, CFI-2000, CFI-2100 und CFI-7000. Das ist keine Behauptung, die Liste sei vollständig. Quelle: [`hardware/README.md`](../hardware/README.md). |
| slim | Von Sony für CFI-2000 und für CFI-2100 verwendeter Zusatz. Keine ausschließliche Zuordnung zu einer Gruppe. |
| PS5 Pro | Von Sony auf der geprüften Einrichtungsseite für die Modellgruppe CFI-7000 verwendet. |
| Systemsoftware | Von Sony verwendeter Name der Konsolensoftware. Quelle: [`firmware-notes/system-software.md`](../firmware-notes/system-software.md). |
| syndicate-research | Dieses öffentliche Repository für veröffentlichungsreife Forschung. |
| syndicate-lab | Privates Repository für interne und unverifizierte Arbeit. |

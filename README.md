# SYNDICATE Research

Öffentliches Repository für verifizierte, veröffentlichungsreife Forschung und technische Dokumentation des Projekts SYNDICATE.

SYNDICATE – Understand. Research. Develop. Document.

## Zweck

Dieses Repository sammelt ausschließlich Inhalte, die geprüft, mit Quelle belegt und zur Veröffentlichung freigegeben sind. Es beschreibt keine fertige Plattform und kündigt keine Funktionen an.

Der aktuelle Stand ist Phase 1 (Foundation): Ordnerstruktur und Arbeitsregeln. Weitere Forschungsphasen sind nicht begonnen.

## Abgrenzung zu syndicate-lab

| Repository | Rolle |
| --- | --- |
| `syndicate-ps5/syndicate-research` (dieses Repository, öffentlich) | Veröffentlichungsreife, verifizierte Forschungsdokumentation |
| `syndicate-ps5/syndicate-lab` (privat) | Interne Entwicklung sowie unverifizierte und noch nicht freigegebene Forschungsdaten |
| `syndicate-ps5/syndicate-ps5.github.io` (öffentlich) | Website des Projekts, getrennt von dieser Dokumentation |

Interne Messungen, Entwürfe, Logs und nicht freigegebene Auswertungen bleiben in `syndicate-lab`. Ein Eintrag wandert erst hierher, wenn Quelle, Evidenzstufe und Veröffentlichungsfreigabe vorliegen.

## Statusdefinitionen

Jede Aufgabe trägt genau einen Status:

| Status | Bedeutung |
| --- | --- |
| Planned | Vorgesehen, noch nicht begonnen |
| In Progress | In Arbeit |
| Implemented | Umgesetzt, aber noch nicht als verifiziert abgeschlossen |
| Tested | Ein nachvollziehbarer Test wurde ausgeführt |
| Verified | Ergebnis wurde gegen die festgelegte Grundlage bestätigt |
| Blocked | Durch eine offene Abhängigkeit aufgehalten |

**Implemented bedeutet nicht automatisch Verified.**

Sachaussagen tragen zusätzlich eine Evidenzstufe. Die Stufen und die Aufnahmeregeln stehen in [`methodology/README.md`](methodology/README.md) und [`glossary/README.md`](glossary/README.md).

## Struktur

```text
.
├── README.md
├── SECURITY.md
├── CONTRIBUTING.md
├── .gitignore
├── docs/
├── hardware/
│   ├── cfi-1000/
│   ├── cfi-2000/
│   └── cfi-7000/
├── firmware-notes/
├── architecture/
├── development-notes/
├── methodology/
├── references/
└── glossary/
```

Jeder Ordner enthält eine `README.md` mit Zweck und Aufnahmeregel. Der einzige aufgenommene Sachinhalt sind die Modellgruppen, die Sony in der USB-Ports-Anleitung nennt. Siehe [`hardware/README.md`](hardware/README.md).

## Lizenz

Eine `LICENSE`-Datei ist bewusst nicht enthalten. Die Lizenzwahl ist eine offene Entscheidung des Owners. Bis zu dieser Entscheidung räumt das Repository keine weitergehende Nutzung ein.

## Sicherheit und Mitarbeit

Sicherheitsmeldungen und Arbeitsgrenzen: [`SECURITY.md`](SECURITY.md).

Verifikationspflicht, Quellenpflicht und Lizenzprüfung bei Fremdinhalten: [`CONTRIBUTING.md`](CONTRIBUTING.md).

# SYNDICATE Research

Öffentliches Repository für verifizierte, veröffentlichungsreife Forschung und technische Dokumentation des Projekts SYNDICATE.

SYNDICATE – Understand. Research. Develop. Document.

## Zweck

Dieses Repository sammelt ausschließlich Inhalte, die geprüft, mit Quelle belegt und zur Veröffentlichung freigegeben sind. Es beschreibt keine fertige Plattform und kündigt keine Funktionen an.

Der aktuelle Stand ist Phase 2 (Research). Die Notizen beschränken sich auf abgerufene Primärquellen. Offene Punkte sind Unknown oder Researching.

## Abgrenzung

| Repository | Rolle |
| --- | --- |
| `syndicate-ps5/syndicate-research` (dieses Repository, öffentlich) | Veröffentlichungsreife, verifizierte Forschungsdokumentation |
| `syndicate-ps5/syndicate-ps5.github.io` (öffentlich) | Website des Projekts, getrennt von dieser Dokumentation |

Öffentliche Forschung in diesem Repository und interne Entwicklung sind getrennt. Ein Eintrag wandert erst hierher, wenn Quelle, Evidenzstufe und Veröffentlichungsfreigabe vorliegen.

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
├── LICENSING.md
├── LICENSES/
│   └── Apache-2.0.txt
├── hardware/
│   ├── cfi-1000/
│   ├── cfi-2000/
│   ├── cfi-2100/
│   └── cfi-7000/
├── firmware-notes/
├── architecture/
├── development-notes/
├── methodology/
├── references/
└── glossary/
```

Jeder Ordner enthält eine `README.md` mit Zweck und Aufnahmeregel. Belegte Modellgruppen, die Systemsoftware-Liste und die engen Architekturaussagen stehen in den jeweiligen Ordnern.

## Lizenz

Die Aufteilung ist in [`LICENSING.md`](LICENSING.md) vorbereitet: CC BY 4.0 für eigene Texte und Dokumentation, Apache-2.0 für eigenen Softwarecode. Eine Root-Datei `LICENSE` gibt es nicht, damit die Aufteilung nicht als Einzellizenz erscheint. Zitate bleiben bei ihren Rechteinhabern.

## Sicherheit und Mitarbeit

Sicherheitsmeldungen und Arbeitsgrenzen: [`SECURITY.md`](SECURITY.md).

Verifikationspflicht, Quellenpflicht und Lizenzprüfung bei Fremdinhalten: [`CONTRIBUTING.md`](CONTRIBUTING.md).

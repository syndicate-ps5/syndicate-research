# Mitwirken

Beiträge zu diesem Repository sind willkommen, wenn sie verifiziert, quellenbelegt und veröffentlichungsreif sind. Interne und unverifizierte Arbeit gehört in das private Repository `syndicate-lab`.

## Verifikationspflicht

Jede sachliche Aussage braucht:

- eine Evidenzstufe aus [`methodology/README.md`](methodology/README.md),
- einen Aufgabenstatus aus der [README](README.md),
- eine nachvollziehbare Quelle.

**Implemented bedeutet nicht automatisch Verified.** Ein umgesetzter Text, ein Skript oder ein Testaufbau wird erst dann als Verified geführt, wenn die dafür festgelegte Prüfung erfolgt ist.

Unverified-Material und reine Internally-Tested-Notizen bleiben in `syndicate-lab`, bis der Owner die Veröffentlichung freigibt. Was eine Quelle nicht hergibt, wird als Unknown gekennzeichnet oder weggelassen. Kompatibilität wird nicht angenommen.

## Quellenpflicht

- Primärquellen haben Vorrang vor Zusammenfassungen.
- Quelle, Abrufdatum und der übernommene Sachumfang stehen am Eintrag.
- Zitate bleiben kurz. Fremde Texte werden nicht in größerem Umfang übernommen.
- Aussagen, die in der Quelle fehlen, werden nicht ergänzt.

## Lizenzprüfung bei Fremdinhalten

Vor der Übernahme von Texten, Daten, Abbildungen oder Code aus fremden Projekten ist die Lizenz zu prüfen.

- Die Lizenz muss die konkrete Nutzung erlauben.
- Herkunft, Lizenzname und Fundstelle stehen im Beitrag.
- Inhalte ohne erkennbare Lizenz werden nicht übernommen.
- Proprietäre Materialien werden nicht über den kurzen, quellengebundenen Sachverhalt hinaus abgeschrieben.

Die Lizenzaufteilung steht in [`LICENSING.md`](LICENSING.md). Eigene Texte stehen unter CC BY 4.0, eigener Softwarecode unter Apache-2.0. Eine Root-Datei `LICENSE` wird nicht ergänzt, solange sie die Aufteilung verdecken würde. Fremde Zitate werden durch diese Lizenzen nicht neu lizenziert.

## Was nicht eingereicht wird

- Geheimnisse, Schlüssel, Tokens, Passwörter und private Daten
- Exploits, Payloads und Anleitungen zur Umgehung von Schutzmechanismen
- unveröffentlichte Schwachstellen
- Produktversprechen und Release-Ankündigungen
- Forschungsdaten ohne Quellenangabe oder ohne Veröffentlichungsfreigabe

Sicherheitsfunde folgen [`SECURITY.md`](SECURITY.md).

## Sprache und Form

Dokumentation ist auf Deutsch. Die festgelegten Status- und Evidenzbegriffe bleiben auf Englisch. Jeder neue Ordner erhält eine kurze `README.md` mit Zweck und Aufnahmeregel.

## Ablauf

Änderungen erfolgen per Pull Request nach `main`. Die Prüfung achtet auf Quelle, Evidenzstufe, Lizenz der Fremdinhalte und darauf, dass keine internen Daten aus `syndicate-lab` enthalten sind.

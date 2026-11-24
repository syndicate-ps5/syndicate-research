# Prüfung und Veröffentlichung

## Zweck

Dieses Dokument beschreibt, wie ein neuer Forschungssatz geprüft und in dieses öffentliche Repository aufgenommen wird. Es ändert die Evidenzstufen in [`methodology/README.md`](../methodology/README.md) nicht.

## Aufnahmeregel

Aufgenommen werden nur verifizierte Inhalte mit Quellenangabe. Interne oder unverifizierte Daten bleiben außerhalb dieses Repositories.

## Prüfung

Jede technische Aussage bekommt eine Quelle, ein Abrufdatum und eine Evidenzstufe. Der übernommene Wortlaut wird an der Primärquelle erneut gelesen. Was die Quelle nicht sagt, wird Unknown oder, solange die Prüfung offen ist, Researching. Eine Vermutung wird nicht als Publicly Documented eingetragen.

Hardware und Firmware bleiben getrennte Sammlungen. Eine Kompatibilitätsaussage braucht einen Satz, der Modellgruppe und Firmwareversion gemeinsam nennt. Fehlt dieser Satz, bleibt die Kombination Unknown. Ein Eintrag in [`data/research.json`](../data/research.json) belegt nur seinen Wortlaut. Er ist kein Installationstest.

Neue Daten folgen [`data/schema.json`](../data/schema.json). Bestehende Notizen werden nicht stillschweigend ersetzt. Eine Ergänzung verweist auf die ältere Notiz und nennt, was hinzukommt.

Geheimnisse, Exploit-Beschreibungen und Anleitungen zur Umgehung von Schutzmechanismen werden nicht aufgenommen. Sicherheitsmeldungen folgen [`SECURITY.md`](../SECURITY.md).

## Veröffentlichung

Ein Satz kann in einem Branch stehen und damit Implemented sein. **Implemented bedeutet nicht automatisch Verified.** Verified setzt den abgeschlossenen Abgleich mit der festgelegten Grundlage voraus. Bei Publicly Documented ist das der erneute Abgleich mit der Primärquelle.

Die Aufnahme in `main` braucht die Freigabe des Owners. Ein Prüf-Branch und ein offener Pull Request sind keine Veröffentlichung und kein Release. Eigene Texte stehen unter CC BY 4.0, eigener Softwarecode unter Apache-2.0, wie in [`LICENSING.md`](../LICENSING.md) beschrieben. Zitate werden dadurch nicht neu lizenziert.

## Ablehnung

Abgelehnt werden Sätze ohne Quelle, erfundene Firmware-Funktionen, aus einer Modellgruppe abgeleitete Kompatibilität und interne Daten ohne Freigabe.

# Forschungsdaten

## Zweck

Dieser Ordner legt das einheitliche Datenformat für Modelle, Firmware, Quellen und Kompatibilität fest und enthält die dazu erfassten Sätze. Die bestehenden Notizen in [`hardware/`](../hardware/README.md) und [`firmware-notes/system-software.md`](../firmware-notes/system-software.md) bleiben bestehen. Diese Dateien wiederholen sie in maschinenlesbarer Form und ergänzen die Versionsnummern, die auf der Sony-Liste als Überschriften stehen.

## Aufnahmeregel

Aufgenommen werden nur verifizierte Inhalte mit Quellenangabe. Interne oder unverifizierte Daten gehören ausschließlich in das private Repository. Eine Kombination ohne Eintrag ist Unknown.

## Dateien

[`schema.json`](schema.json) ist das Format in der Fassung 1.0.0. [`research.json`](research.json) ist der Datenbestand vom Abruf 2026-11-24.

Ein Datensatz hat vier Sammlungen. `sources` nennt URL, Abrufdatum und, soweit die Seite es hergibt, ein Veröffentlichungsdatum. `models` nennt Modellgruppe, wörtliche Bezeichnungen und einzelne Verkaufsnummern. `firmware` nennt die Versionsnummer, ihre Position auf der Sony-Liste und nur die Sätze, die hier wörtlich übernommen sind. `compatibility` nennt die Modellgruppen und alle erfassten Firmware-IDs. `defaultStatus` ist Unknown. Nur `entries` sind Ausnahmen.

`featureDetail` ist `Publicly Documented`, wenn zu dieser Version mindestens ein wörtlicher Satz im Datensatz steht. Sonst ist `featureDetail` Unknown. Das Unknown bezieht sich auf den hier nicht übernommenen Merkmalstext, nicht auf die Existenz der Versionsnummer.

`published` ist `null` und `publishedStatus` ist Unknown, wenn die Quelle kein Veröffentlichungsdatum nennt. Das Abrufdatum ist kein Veröffentlichungsdatum.

Die Prüfung und die Aufnahme neuer Sätze stehen in [`docs/pruefung-und-veroeffentlichung.md`](../docs/pruefung-und-veroeffentlichung.md).

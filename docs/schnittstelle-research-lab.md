# Schnittstelle zwischen Research und Lab

Status: Vorschlag. Keine Datenübernahme. Beide Seiten haben diese Schnittstelle noch nicht freigegeben.

## Aufnahmeregel

Aufgenommen werden nur verifizierte Inhalte mit Quellenangabe. Interne oder unverifizierte Daten bleiben außerhalb dieses öffentlichen Repositories. Unknown und Researching bleiben stehen, solange der Beleg fehlt.

## Was jede Seite heute festlegt

Dieses Repository führt die veröffentlichte Datenbasis in [`data/research.json`](../data/research.json) nach [`data/schema.json`](../data/schema.json). Ein fehlender Kompatibilitätseintrag ist Unknown.

Das Labor führt auf `main` von `syndicate-lab` einen lokalen Validator. Er liest drei getrennte Dokumente:

- `compatibility/models.json` gegen `compatibility/schema/compatibility-document.schema.json`
- `compatibility/firmware.json` gegen dasselbe Schema
- `research/sources.json` gegen `research/source-document.schema.json`

Diese drei Dokumente verwenden `schema_version` 1, `record_type` und `entries`. Ihr Bestand auf `main` ist leer. Ein fehlender Laboreintrag ist dort ebenfalls Unknown. Der Validator ist kein vollständiger Draft-2020-12-Prüfer. Diese Datei ändert seine Regeln nicht und kopiert keine Sätze hinüber.

## Vorgeschlagene Abbildung

Erst nach ausdrücklicher Freigabe beider Seiten würde eine Abbildung, keine Verschiebung, so aussehen.

Quellen aus `sources` werden zu Einträgen in `research/sources.json`. `id` wird `source_id`, `retrieved` wird `accessed`. Titel und URL bleiben. Researching kommt in der Laborliste der Evidenz nicht vor und würde nicht als Quelle eingetragen.

Modellgruppen werden nur als Hardware-Einträge in `compatibility/models.json` vorgeschlagen. Dort gibt es kein Firmwarefeld. Firmwareversionen werden nur als Firmware-Einträge in `compatibility/firmware.json` vorgeschlagen. Dort gibt es keinen Modellnamen.

`related_model_entry_id` käme nur für einen Satz infrage, der Modellgruppe und Versionsnummer gemeinsam nennt. Im jetzigen Bestand ist das allein der Satz zu Adaptive Charging, CFI-2000 und `24.06-10.00.00`. Die Sätze mit „PS5 Pro“ bleiben ohne diese Verknüpfung, weil sie die Modellgruppe CFI-7000 nicht nennen.

Publicly Documented würde nur den jeweils abgebildeten Einzelsatz meinen. Die vollständige Funktionsliste einer Version bleibt Unknown und würde nicht als belegt übertragen.

## Was dieser Vorschlag nicht tut

Er verschiebt `data/research.json` nicht auf die Laborpfade. Er füllt die leeren Labordokumente nicht. Er setzt keine Kombination von Unknown auf einen anderen Status. Er ist keine Freigabe zur Aufnahme nach `main`.

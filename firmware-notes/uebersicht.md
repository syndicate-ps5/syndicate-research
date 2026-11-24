# Firmware-Übersicht

## Zweck

Diese Übersicht ordnet die Versionsnummern, die Sony auf der öffentlichen Systemsoftware-Liste als Überschriften führt. Sie ersetzt [`system-software.md`](system-software.md) nicht und ergänzt keine Funktionsbeschreibungen.

## Aufnahmeregel

Aufgenommen werden nur verifizierte Inhalte mit Quellenangabe. Interne oder unverifizierte Daten gehören ausschließlich in das private Repository.

## Bestand vom 2026-11-24

Quelle: <https://www.playstation.com/en-us/support/hardware/ps5/system-software-info/>

Die Seite zeigt 40 Überschriften. Die erste ist `26.07-14.23.00`, die letzte auf der Seite ist `23.01-07.01.00`. Die Reihenfolge im Datenbestand folgt der Seite, beginnend mit der ersten Überschrift. Ein Veröffentlichungsdatum steht an diesen Überschriften nicht. Ob es ältere Versionen gibt, die auf der Seite fehlen, ist Unknown.

Die Nummern, die wörtlichen Sätze und die offene Fragen stehen in [`data/research.json`](../data/research.json). Für `26.07-14.23.00` ist der Satz übernommen, dass Sony von Security-Fixes schreibt, ohne deren Inhalt zu nennen. Für `26.06-14.00.00` und `26.02-13.00.00` ist der Satz übernommen, dass die dort beschriebene Funktion „available only on PS5 Pro“ ist. Für `24.06-10.00.00` ist der Satz übernommen, dass Adaptive Charging für die Modellgruppe CFI-2000 am USB-Type-C-Anschluss genannt wird. Für alle übrigen Nummern ist der Merkmalstext Unknown.

Die Verteilerseite <https://www.playstation.com/en-us/support/hardware/ps5/system-software/> nennt in dem am selben Tag abgerufenen HTML keine Versionsnummer dieser Form. Welche Datei zu welcher Nummer gehört, ist Unknown.

## Kompatibilität

Die Matrix in `research.json` führt die Modellgruppen CFI-1000, CFI-2000, CFI-2100 und CFI-7000 gegen alle 40 erfassten Firmware-IDs. Der Grundstatus ist Unknown.

Ein einziger Eintrag ist Publicly Documented: Version `24.06-10.00.00` und Modellgruppe CFI-2000, beschränkt auf den zitierten Satz zu Adaptive Charging. Der Satz ist kein Beleg dafür, welche Gruppen diese Versionsnummer installieren können.

Die Sätze „available only on PS5 Pro“ bleiben an der Firmware-Nummer stehen. Sie werden nicht als Kompatibilität der Modellgruppe CFI-7000 eingetragen. Diese Zuordnung ist Unknown, auch wenn die Einrichtungsseite die Bezeichnung „PS5 Pro console (CFI-7000 model group)“ führt. Das sind zwei getrennte Quellen und kein gemeinsamer Satz.

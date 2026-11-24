# Plan: Autorenadresse aus der Git-Historie

Die Historie ist nicht umgeschrieben. Dieser Plan wird erst nach einer gesonderten Freigabe ausgeführt.

## Backup

Vor jeder Umschreibung liegt ein vollständiges Bundle der Historie vom 2026-11-24:

- Pfad außerhalb des Repositories: `/cursor/stores/self/syndicate-research-backup/syndicate-research-pre-rewrite-2026-11-24.bundle`
- `git bundle verify` meldet eine vollständige Historie und die Spitze `ff83432220bba31434e6e6925af5fa530775c0e9`
- SHA-256: `9ba767636667b6d89eb121e14013e64829b9b67ac8d07f10912366bb3931acdb`
- Das Bundle ist nicht Teil dieses Repositories und wird nicht committet.

## Betroffene Commits

Geprüft wurden beide Commits auf `main` und der Inhalt aller Blobs.

| Commit | Betroffen | Befund |
| --- | --- | --- |
| `2e4792908dbd09c3edf3022d50264d70b99c1c51` | Ja | Author-Name `syndicate-ps5`. Author-E-Mail und Committer-E-Mail sind dieselbe private Gmail-Adresse. Der Commit enthält nur die erste `README.md`. |
| `ff83432220bba31434e6e6925af5fa530775c0e9` | Nein | Author und Committer sind `cursoragent@cursor.com`. |

Die Gmail-Adresse steht in keinem Dateiinhalt. Sie steht nur in den Metadaten von `2e47929`. Der genaue Wert bleibt in diesem Dokument ungenannt und ist mit `git log -1 --format='%an %ae%n%cn %ce' 2e4792908dbd09c3edf3022d50264d70b99c1c51` lesbar.

Auf `main` gibt es keine Tags. Inzwischen existiert der Branch `cursor/phase-2-research-e5bf` mit Pull Request #1. Dessen zusätzlicher Commit fügt die private Adresse nicht in Dateiinhalte ein. Die Geschichte dieses Branches enthält weiterhin `2e47929` und `ff83432`. Eine spätere Umschreibung von `main` erfordert, Pull Request #1 auf die neue Historie neu aufzusetzen. Diese Umschreibung ist nicht ausgeführt.

## Vorgehen nach Freigabe

1. Das Bundle prüfen und an einem zweiten Ort sichern.
2. Die Ersatzadresse festlegen. Ohne diese Festlegung wird nicht umgeschrieben.
3. Die Historie mit `git filter-repo` über eine Mailmap oder einen E-Mail-Callback ersetzen. Geändert werden Author- und Committer-E-Mail von `2e47929`. Der Name `syndicate-ps5` bleibt, sofern der Owner nichts anderes festlegt.
4. Weil `ff83432` auf `2e47929` aufbaut, ändern sich beide Commit-Hashes, auch wenn der zweite Commit die Gmail-Adresse nicht enthält.
5. Die neuen Bäume mit den alten Bäumen vergleichen. Der Dateiinhalt muss gleich bleiben.
6. Erst danach `main` mit Lease-Force-Push aktualisieren. Vorher keine Force-Push-Variante ohne Lease.

Nicht verwenden: ein manuelles Ändern nur der Arbeitskopie. Das lässt die Adresse in `2e47929` bestehen.

## Auswirkungen

- Jeder Klon, Fork und jede lokale Branch, die `2e47929` oder `ff83432` enthält, behält die Adresse, bis er neu geholt und hart auf die neue `main` gesetzt wird. Ein gewöhnliches `git pull` schlägt nach der Umschreibung fehl oder erzeugt eine Zusammenführung der alten und der neuen Historie.
- Verweise auf die beiden Hashes, einschließlich GitHub-URLs, Review-Kommentare und dieses Dokuments, zeigen nach dem Push nicht mehr auf die aktuelle `main`. Die Commits können bei GitHub noch über die alten URLs erreichbar bleiben.
- Forks und CI-Caches, die vor der Umschreibung geklont haben, behalten die Adresse. GitHub entfernt verwaiste Commits nicht zuverlässig sofort. Eine vollständige Entfernung aus GitHub-Kopien braucht nach dem Push einen eigenen Antrag an den GitHub-Support und das Löschen oder Neuerstellen bekannter Forks.
- Das Backup-Bundle und diese Arbeitskopie behalten die Adresse, bis sie gelöscht werden. Das ist beabsichtigt, damit die Umschreibung rückgängig gemacht werden kann.
- Pull Request #1 auf dem Branch `cursor/phase-2-research-e5bf` muss nach einer späteren Umschreibung neu aufgesetzt werden. Das gilt auch für weitere dann offene Pull Requests. Releases gibt es keine.

## Status

Planned und Blocked, bis der Owner die Umschreibung und die Ersatzadresse freigibt.

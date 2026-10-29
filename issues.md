# Static Code Analysis Issues — Bike-Share Station Manager

The line numbers below refer to the original `bike_share_stations.py` in the assigned repository. Confirm exact messages and line numbers in your local Pylint, Bandit, and Flake8 reports.

| Issue | Type | Original line(s) | Description | Fix approach |
|---|---|---:|---|---|
| SQL injection risk | Security (high) | 302 | Station name and numeric values were concatenated directly into an SQL statement. | Replaced string concatenation with SQLite parameter placeholders (`?`) and a parameter tuple. |
| Weak random PIN | Security (medium) | 1, 319 | `random.randint` is not intended for security-sensitive PIN generation. | Replaced `random` with `secrets.randbelow` to generate the four-digit PIN securely. |
| Mutable default argument | Bug / maintainability | 300 | `log=[]` reuses the same list across calls. | Changed the default to `None` and creates a new list inside the function. |
| Overly broad exception and silent failure | Reliability | 331–337 | `except Exception: pass` hides database errors and makes failures hard to diagnose. | Removed the blanket exception handler; `reset_station` returns whether a row was updated. |
| Missing-row handling | Bug | 339–346 | `hasBikes` dereferences `row[0]` even if the station ID does not exist. | Check `row is not None` before accessing the bike count. |
| Inconsistent naming and formatting | Style | Throughout | CamelCase function names, spacing, and blank-line patterns do not follow conventional Python style. | Renamed functions to `snake_case` and formatted the file consistently. |
| Missing input validation | Reliability | 300–302 | Empty names and invalid capacity/bike counts could be inserted. | Added validation and database constraints for station capacity and bike count. |
| Unused local variable | Code quality | 325 | `summary` is assigned but never used. | Removed the unused variable. |

## Verification note

Run all three tools locally and update this table's line numbers/messages to match the generated reports. Do not claim a finding is cleared until it is absent from the after-report.

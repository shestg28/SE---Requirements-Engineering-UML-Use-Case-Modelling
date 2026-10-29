"""Manage bike-share stations using an in-memory SQLite database."""

import secrets
import sqlite3

DATABASE = sqlite3.connect(":memory:")
DATABASE.execute(
    """
    CREATE TABLE stations (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        capacity INTEGER NOT NULL CHECK (capacity >= 0),
        bikes INTEGER NOT NULL CHECK (bikes >= 0 AND bikes <= capacity)
    )
    """
)


def add_station(name, capacity, bikes, log=None):
    """Add a station and return the updated station-name log."""
    if not name or not name.strip():
        raise ValueError("Station name must not be empty.")
    if capacity < 0:
        raise ValueError("Capacity cannot be negative.")
    if bikes < 0 or bikes > capacity:
        raise ValueError("Bike count must be between zero and capacity.")

    if log is None:
        log = []

    DATABASE.execute(
        "INSERT INTO stations (name, capacity, bikes) VALUES (?, ?, ?)",
        (name.strip(), capacity, bikes),
    )
    log.append(name.strip())
    return log


def rent_bike(station_id):
    """Rent one bike from a station if one is available."""
    row = DATABASE.execute(
        "SELECT bikes FROM stations WHERE id = ?", (station_id,)
    ).fetchone()

    if row is None or row[0] <= 0:
        return False

    DATABASE.execute(
        "UPDATE stations SET bikes = bikes - 1 WHERE id = ?", (station_id,)
    )
    return True


def unlock_pin():
    """Generate a four-digit, cryptographically secure unlock PIN."""
    return secrets.randbelow(9000) + 1000


def full_stations():
    """Return names of stations where every dock is occupied by a bike."""
    rows = DATABASE.execute(
        "SELECT name FROM stations WHERE bikes = capacity ORDER BY name"
    ).fetchall()
    return [row[0] for row in rows]


def reset_station(station_id):
    """Reset the bike count at a station; return whether it existed."""
    cursor = DATABASE.execute(
        "UPDATE stations SET bikes = 0 WHERE id = ?", (station_id,)
    )
    return cursor.rowcount > 0


def has_bikes(station_id):
    """Return True if the station exists and has at least one bike."""
    row = DATABASE.execute(
        "SELECT bikes FROM stations WHERE id = ?", (station_id,)
    ).fetchone()
    return row is not None and row[0] > 0


def main():
    """Run a short demonstration of the bike-share station manager."""
    add_station("Central Park", 10, 10)
    add_station("Metro Gate", 8, 2)

    print(rent_bike(2), rent_bike(9))
    print(unlock_pin(), full_stations(), has_bikes(2))
    reset_station(1)


if __name__ == "__main__":
    main()

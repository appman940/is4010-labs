
"""JSON-backed, case-insensitive favorite weather locations."""

import json
from pathlib import Path


class FavoritesManager:
    def __init__(self, filename):
        self.filename = Path(filename)
        self.favorites = {}

        try:
            with self.filename.open("r", encoding="utf-8") as file:
                data = json.load(file)

            if isinstance(data, dict):
                self.favorites = {
                    name.lower(): location
                    for name, location in data.items()
                    if isinstance(name, str) and isinstance(location, str)
                }
        except (OSError, ValueError, TypeError):
            self.favorites = {}

    def _save(self):
        with self.filename.open("w", encoding="utf-8") as file:
            json.dump(self.favorites, file, indent=2)

    def add(self, name, location):
        key = name.lower()

        if key in self.favorites:
            return False

        self.favorites[key] = location
        self._save()
        return True

    def remove(self, name):
        key = name.lower()

        if key not in self.favorites:
            return False

        del self.favorites[key]
        self._save()
        return True

    def list_all(self):
        return dict(self.favorites)

    def get_location(self, name):
        return self.favorites.get(name.lower())

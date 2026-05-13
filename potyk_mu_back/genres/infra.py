import json
import sqlite3

from potyk_mu_back.genres.entities import Genre


class GenreRepo:
    def __init__(self, cursor: sqlite3.Cursor):
        self.cursor = cursor

    def list_genres(self) -> list[Genre]:
        rows = self.cursor.execute("SELECT * FROM genres").fetchall()
        return [
            Genre(
                id=row["id"],
                title=row["title"],
                description=row["description"],
                matching_tags=json.loads(row["matching_tags"]),
                text_color=row["text_color"],
                bg_color=row["bg_color"],
            )
            for row in rows
        ]

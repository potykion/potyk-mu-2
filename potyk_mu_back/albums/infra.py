import json
import sqlite3

from potyk_mu_back.albums.entities import Album


class AlbumRepo:
    def __init__(self, cursor: sqlite3.Cursor):
        self.cursor = cursor

    def list_albums(self):
        rows = self.cursor.execute("SELECT * FROM albums").fetchall()
        return [
            Album(
                id=row["id"],
                title=row["title"],
                artist=row["artist"],
                year=row["year"],
                tags=json.loads(row["tags"]),
                yandex_music_url=row["yandex_music_url"],
                rym_url=row["rym_url"],
                cover_url=row["cover_url"],
                comment=row["comment"] or "",
                fav_tracks=json.loads(row["fav_tracks"] or "[]"),
                track_path=row["track_path"],
            )
            for row in rows
        ]

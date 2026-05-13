from dataclasses import dataclass


@dataclass()
class Album:
    id: int
    title: str
    artist: str
    year: int
    tags: list[str]
    yandex_music_url: str
    rym_url: str
    cover_url: str
    comment: str
    fav_tracks: list[str]

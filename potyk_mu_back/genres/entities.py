from dataclasses import dataclass

from potyk_mu_back.albums.entities import Album


@dataclass()
class Genre:
    id: int
    title: str
    description: str
    matching_tags: list[str]
    text_color: str
    bg_color: str

    def match_album(self, album: Album) -> bool:
        return bool(frozenset(self.matching_tags) & frozenset(album.tags))

    def remove_matching_tags(self, album: Album) -> list[str]:
        return list(frozenset(album.tags) - frozenset(self.matching_tags))

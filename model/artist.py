from dataclasses import dataclass

@dataclass
class Artist:
    artist_id: int
    name: str

    def __hash__(self):
        return self.artist_id

    def __eq__(self, other):
        return self.artist_id == other.artist_id

    def __str__(self):
        return f"{self.artist_id} - {self.name}"
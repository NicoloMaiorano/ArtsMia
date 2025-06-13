from dataclasses import dataclass

@dataclass
class Exhibition:
    exhibition_id: int
    exhibition_department: str
    exhibition_title: str
    begin: int
    end: int

    def __hash__(self):
        return self.exhibition_id

    def __eq__(self, other):
        return self.exhibition_id == other.exhibition_id

    def __str__(self):
        return f"{self.exhibition_id} - {self.exhibition_title}"
from dataclasses import dataclass, asdict


@dataclass
class Datafile:
    id: int
    filename: str

    def get_fields_as_dict(self):
        return asdict(self)

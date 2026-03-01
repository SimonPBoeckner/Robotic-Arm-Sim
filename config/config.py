from dataclasses import dataclass, field
from typing import Dict

@dataclass
class Config:
    length_1: float = 1
    length_2: float = 1

    base_coordinate: Dict[float, float] = field(default_factory=lambda: {
        "x": 0,
        "y": 0
    })
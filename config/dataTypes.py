from dataclasses import dataclass
from typing import Dict

@dataclass
class EndEffectorPosition:
    x: float
    y: float

@dataclass
class JointPositions:
    joint_1: Dict[float, float]
    joint_2: Dict[float, float]

@dataclass
class PolarCoordinate:
    theta: float
    length: float
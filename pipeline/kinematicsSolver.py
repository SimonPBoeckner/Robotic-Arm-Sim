from config.dataTypes import EndEffectorPosition, PolarCoordinate
from config.config import Config
from typing import Dict, Optional

import math

class InverseKinematicsSolver():
    def __init__(self, config: Config = None) -> None:
        if config is None:
            self.config = Config()
        else:
            self.config = config

    def solve(self, goal: EndEffectorPosition) -> Dict[PolarCoordinate]:
        r = self.r(goal.x, goal.y)

        if r > self.config.length_1 + self.config.length_2:
            return None
        if r < abs(self.config.length_1 - self.config.length_2):
            return None

        cos_t2 = (goal.x**2 + goal.y**2 - self.config.length_1**2 - self.config.length_2**2) / (2 * self.config.length_1 * self.config.length_2)
        # cos_t2 = max(-1.0, min(1.0, cos_t2))
        t2_base = math.acos(cos_t2)

        sign = -1 if goal.x >= 0 else 1
        t2 = sign * t2_base
        beta = math.atan2(
            self.config.length_2 * math.sin(t2),
            self.config.length_1 + self.config.length_2 * math.cos(t2)
        )
        t1 = math.atan2(goal.y, goal.x) - beta
        print(f"")

        return {
            "joint_1": PolarCoordinate(t1, self.config.length_1),
            "joint_2": PolarCoordinate(t1 + t2, self.config.length_2)
        }

    def r(self, x: float, y: float) -> float:
        return math.sqrt(x**2 + y**2)
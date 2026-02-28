from config.dataTypes import EndEffectorPosition
from config.config import Config

import math

class InverseKinematicsSolver():
    def __init__(self, config: Config = None):
        if config == None:
            self.config = Config()
        else:
            self.config = config

    def solve(self, goal: EndEffectorPosition):
        pass

    def theta_1(self, x: float, y: float):
        self.theta_1 = abs(
            math.acos(
                (math.pow(
                    x, 
                    2
                ) + 
                math.pow(
                    y, 
                    2
                ) -
                math.pow(
                    self.config.length_1,
                    2
                ) -
                math.pow(
                    self.config.length_2,
                    2
                )) /
                (
                    2 * self.config.length_1 * self.config.length_2
                )
            )
        )
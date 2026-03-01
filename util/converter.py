from config.config import Config
from config.dataTypes import PolarCoordinate, JointPositions
from typing import Dict

import math

class Converter():
    def __init__(self, config: Config = None) -> None:
        if config == None:
            self.config = Config()
        else:
            self.config = config

    def polarToCartesian(self, coordinates: Dict[PolarCoordinate, PolarCoordinate]) -> JointPositions:
        joint_1 = {
            "x": coordinates["joint_1"].length * math.cos(coordinates["joint_1"].theta),
            "y": coordinates["joint_1"].length * math.sin(coordinates["joint_1"].theta)
        }
        joint_2 = {
            "x": coordinates["joint_2"].length * math.cos(coordinates["joint_2"].theta),
            "y": coordinates["joint_2"].length * math.sin(coordinates["joint_2"].theta)
        }
        return JointPositions(joint_1, joint_2)
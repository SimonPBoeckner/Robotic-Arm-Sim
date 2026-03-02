from config.config import Config
from config.dataTypes import PolarCoordinate, JointPositions
from typing import Dict, List

import numpy as np
import math

class Converter():
    def __init__(self, config: Config = None) -> None:
        if config == None:
            self.config = Config()
        else:
            self.config = config

    def polarToCartesian(self, coordinates: Dict[str, PolarCoordinate]) -> JointPositions:
        joint_1 = {
            "x": coordinates["joint_1"].length * math.cos(coordinates["joint_1"].theta),
            "y": coordinates["joint_1"].length * math.sin(coordinates["joint_1"].theta)
        }
        joint_2 = {
            "x": coordinates["joint_2"].length * math.cos(coordinates["joint_2"].theta),
            "y": coordinates["joint_2"].length * math.sin(coordinates["joint_2"].theta)
        }
        return JointPositions(joint_1, joint_2)
    
    def polarToList(self, theta_1: float, theta_2: float, coordinates: Dict[str, PolarCoordinate]) -> List:
        segment_1 = np.linspace(theta_1, coordinates["joint_1"].theta, 100)
        print(segment_1)
        segment_2 = np.linspace(theta_2, coordinates["joint_2"].theta, 100)
        print(segment_2)

        return [segment_1, segment_2]
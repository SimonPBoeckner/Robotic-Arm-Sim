import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import math

from config.dataTypes import PolarCoordinate
from config.config import Config
from typing import List, Dict

class Grapher():
    def __init__(self, config : Config = None) -> None:
        if config == None:
            self.config = Config()
        else:
            self.config = config

        self.coords_1: List[float] = [math.pi/2, self.config.length_1]
        print(self.coords_1)
        self.coords_2: List[float] = [math.pi/2, self.config.length_2]
        print(self.coords_2)
        self.lim = (self.config.length_2 + self.config.length_1) * 2

        self.point_1: List[float] = [
            self.coords_1[1] * math.cos(self.coords_1[0]), 
            self.coords_1[1] * math.sin(self.coords_1[0])
        ]
        print(self.point_1)
        self.point_2: List[float] = [
            self.coords_2[1] * math.cos(self.coords_2[0]),
            self.coords_2[1] * math.sin(self.coords_2[0])
        ]
        print(self.point_2)

        plt.ion()

        self.fig = plt.figure(figsize=(10, 6))
        self.ax = self.fig.add_subplot()
        self.ax.set_xlim(-self.lim, self.lim)
        self.ax.set_ylim(0, self.lim)

        self.ax.plot([0, self.point_1[0]], [0, self.point_1[1]])
        self.ax.plot([self.point_1[0], self.point_1[0] + self.point_2[0]], [self.point_1[1], self.point_1[1] + self.point_2[1]])
        self.ax.plot([-self.config.length_2 * 100, -self.config.length_2 * 100], [0, self.config.length_2 * 100])
        self.ax.plot([-self.config.length_2 * 100, self.config.length_2 * 100], [-self.config.length_2 * 100, -self.config.length_2 * 100])

        self.anim = animation.FuncAnimation(
            self.fig,
            self.animate,
            interval=100
        )

    def animate(self, i) -> None:
        self.ax.clear()
        self.ax.plot([-self.config.length_2 * 100, -self.config.length_2 * 100], [0, self.config.length_2 * 100])
        self.ax.plot([-self.config.length_2 * 100, self.config.length_2 * 100], [-self.config.length_2 * 100, -self.config.length_2 * 100])
        self.ax.plot([0, self.point_1[0]], [0, self.point_1[1]])
        self.ax.plot([self.point_1[0], self.point_1[0] + self.point_2[0]], [self.point_1[1], self.point_1[1] + self.point_2[1]])
        self.ax.set_xlim(-self.lim, self.lim)
        self.ax.set_ylim(0, self.lim)

    def update(self, points: Dict[PolarCoordinate]) -> None:
        self.coords_1[0] = points["joint_1"].theta
        self.coords_2[0] = points["joint_2"].theta
        self.point_1[0] = math.cos(points["joint_1"].theta) * points["joint_1"].length
        self.point_1[1] = math.sin(points["joint_1"].theta) * points["joint_1"].length
        print(f"x {self.point_1[0]}, y: {self.point_1[1]}")
        self.point_2[0] = math.cos(points["joint_2"].theta) * points["joint_2"].length
        self.point_2[1] = math.sin(points["joint_2"].theta) * points["joint_2"].length
        print(f"x: {self.point_2[0]}, y: {self.point_2[1]}")

    def start(self) -> None:
        plt.show(block=False)
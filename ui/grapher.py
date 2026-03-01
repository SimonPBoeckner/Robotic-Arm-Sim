import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

from config.dataTypes import JointPositions
from config.config import Config
from typing import List

class Grapher():
    def __init__(self, config : Config = None) -> None:
        if config == None:
            self.config = Config()
        else:
            self.config = config

        self.point_1: List[float, float] = [0, self.config.length_1]
        self.point_2: List[float, float] = [0, self.config.length_2]
        self.lim = (self.config.length_2 + self.config.length_1) * 2

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

    def update(self, points: JointPositions) -> None:
        self.point_1[0] = points.joint_1["x"]
        self.point_1[1] = points.joint_1["y"]
        self.point_2[0] = points.joint_2["x"]
        self.point_2[1] = points.joint_2["y"]

    def start(self) -> None:
        plt.show(block=False)
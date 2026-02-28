import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

from config.dataTypes import EndEffectorPosition
from config.config import Config

class Grapher():
    def __init__(self, config : Config = None):
        if config == None:
            self.config = Config()
        else:
            self.config = config

        self.fig = plt.figure()
        self.ax = self.fig.add_subplot()
        self.ax.plot()

        self.anim = animation.FuncAnimation(
            self.fig,
            self.animate,
            interval=100
        )

    def animate(self, i):
        self.ax.clear()
        self.ax.plot([np.random.randint(0,10), np.random.randint(0,10)])

    def start(self):
        plt.show()
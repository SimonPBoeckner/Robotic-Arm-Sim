import sys
import threading
import time
import matplotlib.pyplot as plt

from ui.grapher import Grapher
from config.config import Config
from pipeline.kinematicsSolver import InverseKinematicsSolver
from config.dataTypes import EndEffectorPosition, PolarCoordinate
from util.converter import Converter

config = Config()
solver = InverseKinematicsSolver()
converter = Converter()
grapher = Grapher()
grapher.start()

def input_loop():
    try:
        while True:
            sys.stdout.write('Enter X coordinate: ')
            sys.stdout.flush()
            x = sys.stdin.readline().strip()

            sys.stdout.write('Enter Y coordinate: ')
            sys.stdout.flush()
            y = sys.stdin.readline().strip()

            result = solver.solve(EndEffectorPosition(float(x), float(y)))
            if result is None:
                print('Position Invalid')
                continue

            frames = converter.polarToList(grapher.coords_1[0], grapher.coords_2[0], result)

            for frame in range(len(frames[0])):
                joint = {
                    "joint_1": PolarCoordinate(frames[0][frame], config.length_1),
                    "joint_2": PolarCoordinate(frames[1][frame], config.length_2)
                }
                grapher.update(joint)
                time.sleep(0.05)

    except Exception as e:
        import traceback
        traceback.print_exc()

t = threading.Thread(target=input_loop, daemon=True)
t.start()

while True:
    plt.pause(0.1)
from ui.grapher import Grapher
from pipeline.kinematicsSolver import InverseKinematicsSolver
from config.dataTypes import EndEffectorPosition, JointPositions
from util.converter import Converter
from typing import Dict

solver = InverseKinematicsSolver()
position: JointPositions

converter = Converter()

grapher = Grapher()
grapher.start()

while True:
    x, y = input('enter X coordinate: '), input('enter Y coordinate: ')
    result = solver.solve(EndEffectorPosition(float(x), float(y)))
    if result is None:
        print('Position Invalid')
        continue
    else:
        position = result
        grapher.update(converter.polarToCartesian(position))
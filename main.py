from ui.grapher import Grapher
from pipeline.kinematicsSolver import InverseKinematicsSolver
from config.dataTypes import EndEffectorPosition

solver = InverseKinematicsSolver()

grapher = Grapher()
grapher.start()

while True:
    x, y = input('enter X coordinate: '), input('enter Y coordinate: ')
    solver.solve(EndEffectorPosition[float(x), float(y)])


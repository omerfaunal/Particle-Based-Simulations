import numpy as np
from models import SimulationResult


def write_file(name, simulation: SimulationResult):
    with open(name, 'w') as f:
        for i in range(len(simulation.absorved_timeline)):
            f.write(str(simulation.absorved_timeline[i]) + '\n')


def read_file(name):
    with open(name, 'r') as f:
        return np.array(list(map(float, f.readlines())))

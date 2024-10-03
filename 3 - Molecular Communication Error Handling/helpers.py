import numpy as np
from models import SimulationResult


def write_file(name, simulation: SimulationResult):
    with open(name, 'w') as f:
        for i in range(len(simulation.absorved_timeline)):
            f.write(str(simulation.absorved_timeline[i]) + '\n')


def read_file(name):
    with open(name, 'r') as f:
        return np.array(list(map(float, f.readlines())))


def write_file_bit(name, simulation: SimulationResult):
    with open(name, 'w') as f:
        f.write(str(simulation.parameters.bit_count) + '\n')
        for i in range(len(simulation.real_bit)):
            f.write(str(simulation.real_bit[i]))
        f.write('\n')
        for i in range(len(simulation.received_bit)):
            f.write(str(simulation.received_bit[i]))
        f.write('\n')
        for i in range(len(simulation.absorved_timeline1)):
            f.write(str(simulation.absorved_timeline1[i]) + '\n')
        for i in range(len(simulation.absorved_timeline2)):
            f.write(str(simulation.absorved_timeline2[i]) + '\n')


def read_file_bit(name):
    with open(name, 'r') as f:
        bit_count = int(f.readline().strip())
        real_bit = list(map(int, f.readline().strip()))
        received_bit = list(map(int, f.readline().strip()))
        absorved_timeline1 = np.array(
            list(map(float, f.readlines()))[:bit_count])
        absorved_timeline2 = np.array(
            list(map(float, f.readlines()))[:bit_count])
        return SimulationResult(absorved_timeline1, absorved_timeline2, real_bit, received_bit, None, None)

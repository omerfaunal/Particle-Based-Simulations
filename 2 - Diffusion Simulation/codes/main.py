from simulator import AbsorbingSphereDiffusionSimulator
from models import SimulationResult
from parameters import *
import draw
from helpers import write_file, read_file


def simulate_from_file():
    # For easier plotting, you can simulate the result from a file
    time = read_file('time.txt')

    simulation1_2 = SimulationResult(
        read_file('task2_1_2.txt'), time, parameter_set_task2_1_2)
    simulation1_3 = SimulationResult(
        read_file('task2_1_3.txt'), time, parameter_set_task2_1_3)

    draw.plot_two(simulation1_2, simulation1_3)


def simulate_from_scratch():
    # Define the parameters for the simulation
    # and simulate the result
    simulation2_1_3 = AbsorbingSphereDiffusionSimulator(
        parameter_set_task2_1_3, is2D=True).simulate()

    write_file('task2_1_3.txt', simulation2_1_3)

    draw.plot_one(simulation2_1_3)


simulate_from_file()

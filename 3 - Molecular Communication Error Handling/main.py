from simulator import AbsorbingSphereDiffusionSimulator
from models import SimulationResult
from parameters import *
import draw
from helpers import write_file_bit, read_file_bit


def simulate_from_file():
    # For easier plotting, you can simulate the result from a file
    result = read_file_bit("first_bit.txt")


def simulate_from_scratch():
    # Define the parameters for the simulation
    # and simulate the result
    simulation = AbsorbingSphereDiffusionSimulator(
        parameter_set_task2_1_1).simulate()

    for i in range(len(simulation.received_bit)):
        if i % 2 == 0:
            received_molecule_count = simulation.absorved_timeline1[i]
        else:
            received_molecule_count = simulation.absorved_timeline2[i]
        print(
            f"Bit {simulation.real_bit[i]}: {simulation.received_bit[i]} received molecule count {received_molecule_count}")

    # Count of real_bit == received_bit
    count = sum(1 for real, received in zip(simulation.real_bit,
                simulation.received_bit) if real == received)
    print(f"Count of real_bit == received_bit: {count}")

    write_file_bit('first_bit.txt', simulation)


simulate_from_scratch()

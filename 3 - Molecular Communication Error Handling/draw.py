import matplotlib.pyplot as plt
from simulator import SimulationResult


def plot_one(simulation: SimulationResult, theoretical_value: bool = False):
    # Plot the simulation with color blue
    plt.plot(simulation.time, simulation.absorved_timeline,
             'b', label="Experiment")
    if theoretical_value:
        # Get the theoretical value
        theoretical_value = calculate_theoretical_value(simulation)
        # Plot the theoretical value with color green
        plt.plot(simulation.time, theoretical_value, 'g', label="Theory")
    plt.xlabel('Time')
    plt.ylabel('Cumulative Number of Molecules Hitting the Receiver')
    plt.title('Molecule Simulation D = {}'.format(simulation.parameters.D))
    plt.legend()
    plt.show()


def plot_two(simulation1: SimulationResult, simulation2: SimulationResult):
    # Plot the simulation1 with color blue and label 'D=75'
    plt.plot(simulation1.time, simulation1.absorved_timeline,
             'b', label="Roll Back")
    # Plot the simulation2 with color red
    plt.plot(simulation2.time, simulation2.absorved_timeline,
             'r', label="Reflection")
    plt.xlabel('Time')
    plt.ylabel('Cumulative Number of Molecules Hitting the Receiver')
    plt.title('Molecule Simulation')
    # Add text to bottom
    plt.legend()
    plt.show()


def plot_three(simulation1: SimulationResult, simulation2: SimulationResult, simulation3: SimulationResult):
    plt.plot(simulation1.time, simulation1.absorved_timeline,
             'b', label=f"{simulation1.parameters.reflecting_line.A}, \
                {simulation1.parameters.reflecting_line.B}, {simulation1.parameters.reflecting_line.C}")
    # Plot the simulation2 with color red
    plt.plot(simulation2.time, simulation2.absorved_timeline,
             'r', label=f"{simulation2.parameters.reflecting_line.A}, \
                {simulation2.parameters.reflecting_line.B}, {simulation2.parameters.reflecting_line.C}")
    # Plot the simulation3 with color green
    plt.plot(simulation3.time, simulation3.absorved_timeline,
             'g', label=f"{simulation3.parameters.reflecting_line.A}, \
                {simulation3.parameters.reflecting_line.B}, {simulation3.parameters.reflecting_line.C}")
    plt.xlabel('Time')
    plt.ylabel('Cumulative Number of Molecules Hitting the Receiver')
    plt.title('Molecule Simulation')
    # Add text to bottom
    plt.legend()
    plt.show()


def plot_discrete(simulation1: SimulationResult, simulation2: SimulationResult):
    # Calculate discrete
    simulation1.absorved_timeline, simulation1.time = _calculate_discrete(
        simulation1.absorved_timeline, simulation1.time, 100)
    simulation2.absorved_timeline, simulation2.time = _calculate_discrete(
        simulation2.absorved_timeline, simulation2.time, 100)
    # Plot
    plot_two(simulation1, simulation2)


def _calculate_discrete(timeline, time, time_slot):
    timeline = [timeline[i+time_slot-1] - timeline[i]
                for i in range(0, len(timeline), time_slot)]
    time = [sum(time[i:i+time_slot]) for i in range(0, len(time), time_slot)]
    return timeline, time


def calculate_theoretical_value(result: SimulationResult):
    import math
    import numpy as np
    dist = result.parameters.distance
    rx_r = result.parameters.r
    D = result.parameters.D
    part1 = rx_r / (dist + rx_r)
    nrx_cumulative = result.parameters.num_molecules * part1 * \
        np.vectorize(math.erfc)(dist / np.sqrt(4 * D * result.time))
    return nrx_cumulative

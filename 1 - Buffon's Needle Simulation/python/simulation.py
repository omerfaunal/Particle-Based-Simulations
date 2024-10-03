from constants import D, L, BOARD_HEIGHT
import math
import random
from dataclasses import dataclass


@dataclass
class Needle:
    x_right: float
    x_left: float
    y_up: float
    y_down: float
    theta: float


def throw_needle(L: float):
    x = random.uniform(0, D)
    y = random.uniform(0, (BOARD_HEIGHT - 70) / 100)
    theta = random.uniform(0, math.pi)

    y_up = y + L / 2 * math.cos(theta)
    y_down = y - L / 2 * math.cos(theta)

    x_right = x + L / 2 * math.sin(theta)
    x_left = x - L / 2 * math.sin(theta)

    return Needle(x_right, x_left, y_up, y_down, theta)


def measure_needle(D: float, needle: Needle):
    return needle.x_right > D or needle.x_left < 0


def do_experiment(experiment_count: int):
    hits = 0
    for _ in range(experiment_count):
        needle = throw_needle(L)
        if measure_needle(D, needle):
            hits += 1

    # Calculate the estimated value of pi
    probability = hits / experiment_count
    pi_estimate = 2 * L / (D * probability)

    return probability, pi_estimate

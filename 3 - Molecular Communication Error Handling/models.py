from dataclasses import dataclass


@dataclass
class Line:
    A: float
    B: float
    C: float
    reflection_strategy: str


@dataclass
class SimulationParameters:
    center: float
    r: float
    distance: int
    emission_point: list
    D: float
    tend: float
    delta_t: float
    num_molecules: int
    bit_threshold: int = 50  # To count as 1
    remove_condition: int = 20
    bit_count: int = 1
    reflecting_line: Line = None


@dataclass
class SimulationResult:
    absorved_timeline1: list
    absorved_timeline2: list
    real_bit: list
    received_bit: list
    time: list
    parameters: SimulationParameters

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

    reflecting_line: Line = None


@dataclass
class SimulationResult:
    absorved_timeline: list
    time: list
    parameters: SimulationParameters

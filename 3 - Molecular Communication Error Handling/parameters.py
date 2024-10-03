from models import SimulationParameters, Line
parameter_set_task2_1_1 = SimulationParameters(
    center=[0, 0, 0],
    r=5,
    distance=5,
    emission_point=[10, 0, 0],
    D=75,
    tend=8,
    delta_t=0.0001,
    num_molecules=5000,
    bit_threshold=750,
    bit_count=100,
    remove_condition=20
)

parameter_set_task2_1_2 = SimulationParameters(
    center=[0, 0],
    r=5,
    distance=5,
    emission_point=[10, 0],
    D=75,
    reflecting_line=Line(A=1, B=1, C=-15, reflection_strategy='roll_back'),
    tend=0.6,
    delta_t=0.0001,
    num_molecules=50000
)

parameter_set_task2_1_3 = SimulationParameters(
    center=[0, 0],
    r=5,
    distance=5,
    emission_point=[10, 0],
    D=75,
    reflecting_line=Line(
        A=1, B=1, C=-15, reflection_strategy='reflection_wrt_line'),
    tend=0.6,
    delta_t=0.0001,
    num_molecules=50000
)

parameter_set_task2_2_1 = SimulationParameters(
    center=[0, 0],
    r=5,
    distance=5,
    emission_point=[10, 0],
    D=75,
    tend=0.6,
    delta_t=0.0001,
    num_molecules=50000
)

parameter_set_task2_2_2 = SimulationParameters(
    center=[0, 0],
    r=5,
    distance=5,
    emission_point=[10, 0],
    D=75,
    reflecting_line=Line(A=1, B=1, C=-18, reflection_strategy='roll_back'),
    tend=0.6,
    delta_t=0.0001,
    num_molecules=50000
)

parameter_set_task2_2_3 = SimulationParameters(
    center=[0, 0],
    r=5,
    distance=5,
    emission_point=[10, 0],
    D=75,
    reflecting_line=Line(
        A=1, B=1, C=-18, reflection_strategy='reflection_wrt_line'),
    tend=0.6,
    delta_t=0.0001,
    num_molecules=50000
)

parameter_set_task2_3_1 = SimulationParameters(
    center=[0, 0],
    r=5,
    distance=5,
    emission_point=[10, 0],
    D=75,
    tend=0.6,
    delta_t=0.0001,
    num_molecules=50000
)

parameter_set_task2_3_2 = SimulationParameters(
    center=[0, 0],
    r=5,
    distance=5,
    emission_point=[10, 0],
    D=75,
    reflecting_line=Line(A=1, B=0, C=-15, reflection_strategy='roll_back'),
    tend=0.6,
    delta_t=0.0001,
    num_molecules=50000
)

parameter_set_task2_3_3 = SimulationParameters(
    center=[0, 0],
    r=5,
    distance=5,
    emission_point=[10, 0],
    D=75,
    reflecting_line=Line(
        A=1, B=0, C=-15, reflection_strategy='reflection_wrt_line'),
    tend=0.6,
    delta_t=0.0001,
    num_molecules=50000
)

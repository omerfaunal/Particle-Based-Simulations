import numpy as np
from models import SimulationParameters, SimulationResult


class AbsorbingSphereDiffusionSimulator:
    def __init__(self, parameters: SimulationParameters, is2D: bool = False):
        self.parameters = parameters
        self.is2D = is2D

    def simulate(self):
        # Initialize the simulation
        self.total_absorbed = 0
        self.initialize_particles()

        # Simulate the movement of the particles
        for i in range(1, self.sim_step_count):
            self.move_particles()

            # If reflection is enabled, reflect the particles
            if (self.parameters.reflecting_line):
                self.reflect_particles()

            self.absorve_particles()

            # Update the timeline
            self.timeline[i] += self.total_absorbed

        # Return the result and create timeframe
        time = np.arange(0, self.parameters.tend, self.parameters.delta_t)
        return SimulationResult(self.timeline, time, self.parameters)

    def initialize_particles(self):
        # Calculate the standard deviation of the normal distribution
        self.sigma = (2 * self.parameters.D * self.parameters.delta_t) ** 0.5
        # Initialize the coordinates of the molecules to the emission point
        self.mol_coords_before_movement = np.array(
            [self.parameters.emission_point] * self.parameters.num_molecules)
        # Calculate the square of the radius of the receiver membrane
        self.rx_membrane_sq = self.parameters.r ** 2
        # Calculate the number of simulation steps
        self.sim_step_count = round(
            self.parameters.tend / self.parameters.delta_t)
        # Initialize the timeline
        self.timeline = [0] * self.sim_step_count

    def move_particles(self):
        # Randomly displace the molecules according to the normal distribution
        mol_displacement = np.random.normal(
            0, self.sigma, size=(len(self.mol_coords_before_movement), 3 - self.is2D))
        self.mol_coords_after_movement = self.mol_coords_before_movement + mol_displacement

    def absorve_particles(self):
        # Calculate the distance of the molecules from the receiver center
        dist_sq_2_rcv_center = np.sum(
            (self.mol_coords_after_movement - np.array(self.parameters.center))**2, axis=1)
        # Check if the molecules are inside the receiver membrane
        outside_rx_membrane_mask = dist_sq_2_rcv_center > self.rx_membrane_sq
        # Update the total number of absorbed molecules if they are inside the receiver membrane
        self.total_absorbed += np.count_nonzero(~outside_rx_membrane_mask)
        # Remove the molecules that are absorbed by the receiver
        self.mol_coords_before_movement = self.mol_coords_after_movement[outside_rx_membrane_mask]

    def reflect_particles(self):
        # Find the reflected molecules
        line = self.parameters.reflecting_line
        reflected_mask = self.check_reflected()
        # If there are no reflected molecules, return
        if (np.count_nonzero(reflected_mask) == 0):
            return
        if (line.reflection_strategy == 'roll_back'):
            # If the reflection strategy is roll_back, roll back the reflected molecules
            # Set the coordinates of the reflected molecules to the coordinates before the movement
            self.mol_coords_after_movement[reflected_mask] = self.mol_coords_before_movement[reflected_mask]
        elif (line.reflection_strategy == 'reflection_wrt_line'):
            # If the reflection strategy is reflection_wrt_line, reflect the molecules wrt the reflecting line
            A, B, C = line.A, line.B, line.C
            denominator = A**2 + B**2

            points = self.mol_coords_after_movement[reflected_mask]

            x, y = points[:, 0], points[:, 1]
            # Basically reflect the points at t = t + delta_t wrt the line
            X = x - \
                2 * A * (A * points[:, 0] + B * points[:, 1] + C) / denominator
            Y = y - \
                2 * B * (A * points[:, 0] + B * points[:, 1] + C) / denominator

            self.mol_coords_after_movement[reflected_mask] = np.column_stack(
                (X, Y))

    def check_reflected(self):
        # Check if the molecules are reflected by evaluating the line equation
        def eval_line_sign(x, y):
            # Evaluate the line equation
            return self.parameters.reflecting_line.A * x + self.parameters.reflecting_line.B * y + self.parameters.reflecting_line.C
        sign_before = eval_line_sign(
            self.mol_coords_before_movement[:, 0], self.mol_coords_before_movement[:, 1])
        sign_after = eval_line_sign(
            self.mol_coords_after_movement[:, 0], self.mol_coords_after_movement[:, 1])

        # If the sign of the line equation changes, the molecule is reflected
        reflected_mask = sign_before * sign_after < 0
        return reflected_mask

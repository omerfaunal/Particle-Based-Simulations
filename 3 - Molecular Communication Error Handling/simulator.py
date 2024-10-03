import numpy as np
from models import SimulationParameters, SimulationResult
from particle import Particle


class AbsorbingSphereDiffusionSimulator:
    def __init__(self, parameters: SimulationParameters):
        self.parameters = parameters
        self.timeline1 = []
        self.timeline2 = []
        self.type = 0
        self.count_removed = 0
        self.received_bit = [0] * self.parameters.bit_count
        self.real_bit = [0] * self.parameters.bit_count

    def simulate(self):
        # Initialize the simulation
        self.total_absorbed = 0
        self.initialize_experiment()

        bit = np.random.randint(0, 2)
        self.real_bit[0] = bit
        if bit == 1:
            self.initialize_particles(
                self.parameters.num_molecules)

        # Simulate the movement of the particles
        k = 0
        for i in range(1, self.sim_step_count + 1):

            self.move_particles()

            self.absorve_particles()

            if i % self.bit_rate == 0:
                print(f"Simulation step {i}/{self.sim_step_count}")
                # Update the timeline
                if self.type == 0:
                    self.timeline1[k] = self.count_removed
                    if self.count_removed > self.parameters.bit_threshold:
                        self.received_bit[k] = 1
                else:
                    self.timeline2[k] = self.count_removed
                    if self.count_removed > self.parameters.bit_threshold:
                        self.received_bit[k] = 1
                self.type = 1 - self.type
                self.count_removed = 0

                # Set a random bit to send either 0 or 1

                if (k + 1) < self.parameters.bit_count:
                    bit = np.random.randint(0, 2)
                    self.real_bit[k + 1] = bit
                    if bit == 1:
                        self.initialize_particles(
                            self.parameters.num_molecules)
                print(f"Number of particles: {self.particles.shape[0]}")
                k += 1

        # Return the result and create timeframe
        time = np.arange(0, self.parameters.tend, self.parameters.delta_t)
        return SimulationResult(self.timeline1, self.timeline2, self.real_bit, self.received_bit, time, self.parameters)

    def initialize_experiment(self):
        # Calculate the standard deviation of the normal distribution
        self.sigma = (2 * self.parameters.D * self.parameters.delta_t) ** 0.5
        # Calculate the square of the radius of the receiver membrane
        self.rx_membrane_sq = self.parameters.r ** 2
        # Calculate the number of simulation steps
        self.sim_step_count = round(
            self.parameters.tend / self.parameters.delta_t)
        self.bit_rate = self.sim_step_count // self.parameters.bit_count

        # Initialize 3D empty numpy array
        self.particles = np.empty((0, 4))

        # Initialize timeline with self.sim_step_count // 100 zeros
        self.timeline1 = [0] * (self.sim_step_count // self.bit_rate)
        self.timeline2 = [0] * (self.sim_step_count // self.bit_rate)

        self.center = [(x1 + x2) / 2 for x1,
                       x2 in zip(self.parameters.center, self.parameters.emission_point)]

    def initialize_particles(self, n):
        # Initialize n particles using numpy array parameters.emission_point and type
        particle_template = self.parameters.emission_point + [self.type]
        particles = np.array([particle_template] * n)
        # Append the particles to the list of particles
        self.particles = np.append(self.particles, particles, axis=0)

    def move_particles(self):
        # Randomly displace the molecules according to the normal distribution with shape (n, 3)
        mol_displacement = np.random.normal(
            0, self.sigma, (self.particles.shape[0], 3))
        # Update the firtst 3 columns of the particles array
        self.particles[:, :3] += mol_displacement

    def absorve_particles(self):
        dist = np.linalg.norm(
            self.particles[:, :3] - self.parameters.center, axis=1)

        # Create a boolean mask for particles that meet the conditions
        mask_remove = (dist <= self.parameters.r) & (
            self.particles[:, 3] == self.type)
        self.count_removed += np.count_nonzero(mask_remove)

        # Update self.particles using the mask
        mask = (dist > self.parameters.r) | (self.particles[:, 3] != self.type)

        dist2 = np.linalg.norm(
            self.particles[:, :3] - self.center, axis=1)
        mask_within_threshold = dist2 <= self.parameters.remove_condition
        # Count the number of zeros in mask_within_threshold
        # print(
        #     f"Number of particles within threshold: {len(mask_within_threshold) - np.count_nonzero(mask_within_threshold)}")
        # sum two masks
        mask = mask & mask_within_threshold

        # Update self.particles using the mask
        self.particles = self.particles[mask]

        # Eliminate the particle from the simulation if it is further than the receiver membrane

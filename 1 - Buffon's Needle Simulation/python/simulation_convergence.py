import matplotlib.pyplot as plt
from simulation import do_experiment

# Lists to store pi estimates
pi_estimates = []
probabilities = []
experiment_counts = [100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000]

for experiment in experiment_counts:
    probability, pi_estimate = do_experiment(experiment)

    probabilities.append(probability)
    pi_estimates.append(pi_estimate)

# Plot the convergence of pi
plt.plot(experiment_counts, probabilities, marker='o', linestyle='-', color='r', label='Probability')
plt.xscale('log')  # Use a logarithmic scale for the x-axis to evenly space experiments
plt.xlabel("Number of Experiments (log scale)")
plt.ylabel("Probability")
plt.title("Convergence of Probability")
plt.grid(True, which='both', linestyle='--', linewidth=0.5)  # Add a grid

plt.legend()
plt.show()

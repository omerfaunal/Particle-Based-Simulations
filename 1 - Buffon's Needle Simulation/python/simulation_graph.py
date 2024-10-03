from constants import D, L, BOARD_HEIGHT, LINE_START, LINE_END, PADDING
import tkinter as tk
from simulation import throw_needle, measure_needle

# Create a window
window = tk.Tk()
window.title("Buffon's Needle Simulation")

# Create a canvas on the window
canvas = tk.Canvas(window, width=800, height=500)
canvas.pack()


# Draw two lines
canvas.create_line(LINE_START, 0, LINE_START, BOARD_HEIGHT)
canvas.create_line(LINE_END, 0, LINE_END, BOARD_HEIGHT)

hits = 0
experiment = 10000
for _ in range(experiment):
    needle = throw_needle(L)
    if measure_needle(D, needle):
        canvas.create_line(
            LINE_START + needle.x_right*100, needle.y_up*100 + PADDING, LINE_START + needle.x_left*100, needle.y_down*100 + PADDING, fill="red")
        hits += 1
    else:
        canvas.create_line(
            LINE_START + needle.x_right*100, needle.y_up*100 + PADDING, LINE_START + needle.x_left*100, needle.y_down*100 + PADDING, fill="green")

# Calculate the estimated value of pi
probability = hits / experiment
pi = 2 * L / (D * probability)

# Display the estimated value of pi, hits and miss
experiment_count = tk.Label(window, text=f"Experiment: {experiment}")
experiment_count.pack()
hits_label = tk.Label(window, text=f"Hits: {hits}")
hits_label.pack()
pi_label = tk.Label(window, text=f"Estimated pi: {pi}")
pi_label.pack()

window.mainloop()

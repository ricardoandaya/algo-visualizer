import tkinter as tk
from tkinter import ttk
import importlib
import os
import random


# PLUGIN LOADER

def load_algorithms():

    algorithms = {}

    folder = "algorithms"

    for filename in os.listdir(folder):

        if not filename.endswith(".py"):
            continue

        if filename == "__init__.py":
            continue

        module_name = filename[:-3]

        try:

            module = importlib.import_module(
                f"algorithms.{module_name}"
            )

            if hasattr(module, "NAME") and hasattr(module, "run"):

                algorithms[module.NAME] = module

        except Exception as error:

            print(
                f"Could not load {filename}: {error}"
            )

    return algorithms


# GLOBAL DATA

numbers = [
    45, 12, 78, 23,
    9, 56, 34, 67
]

target = 23

algorithms = load_algorithms()

steps = []
current_step = 0

running = False
paused = False

animation_id = None


# WINDOW
root = tk.Tk()
root.title("Algorithm Visualizer")
root.geometry("1100x700")
root.resizable(False, False)


# TITLE
title_label = tk.Label(
    root,
    text="ALGORITHM VISUALIZER",
    font=("Arial", 26, "bold")
)

title_label.pack(pady=20)


# TOP CONTROL AREA
control_frame = tk.Frame(root)
control_frame.pack(pady=10)


# Algorithm selector
tk.Label(
    control_frame,
    text="Algorithm:",
    font=("Arial", 14)
).grid(
    row=0,
    column=0,
    padx=5
)


algorithm_names = list(algorithms.keys())

algorithm_var = tk.StringVar()

if algorithm_names:
    algorithm_var.set(
        algorithm_names[0]
    )


algorithm_dropdown = ttk.Combobox(
    control_frame,
    textvariable=algorithm_var,
    values=algorithm_names,
    state="readonly",
    width=20,
    font=("Arial", 12)
)

algorithm_dropdown.grid(
    row=0,
    column=1,
    padx=5
)


# Target input
tk.Label(
    control_frame,
    text="Target:",
    font=("Arial", 14)
).grid(
    row=0,
    column=2,
    padx=(20, 5)
)


target_entry = tk.Entry(
    control_frame,
    width=8,
    font=("Arial", 12)
)

target_entry.insert(
    0,
    str(target)
)

target_entry.grid(
    row=0,
    column=3,
    padx=5
)


# CANVAS
canvas = tk.Canvas(
    root,
    width=1000,
    height=300,
    bg="white",
    highlightthickness=1
)

canvas.pack(pady=20)


# STATUS
status_label = tk.Label(
    root,
    text="Ready",
    font=("Arial", 16, "bold")
)

status_label.pack(pady=5)


comparison_label = tk.Label(
    root,
    text="Operations: 0",
    font=("Arial", 14)
)

comparison_label.pack()


# SPEED CONTROL
speed_frame = tk.Frame(root)
speed_frame.pack(pady=10)


tk.Label(
    speed_frame,
    text="Speed:",
    font=("Arial", 13)
).pack(side=tk.LEFT)


speed_scale = tk.Scale(
    speed_frame,
    from_=50,
    to=1500,
    orient=tk.HORIZONTAL,
    length=300,
    label="Delay (ms)"
)

speed_scale.set(500)

speed_scale.pack(
    side=tk.LEFT,
    padx=10
)


# BUTTONS
button_frame = tk.Frame(root)
button_frame.pack(pady=15)

start_button = tk.Button(
    button_frame,
    text="▶ Start",
    width=12,
    font=("Arial", 12),
)

start_button.grid(
    row=0,
    column=0,
    padx=5
)


pause_button = tk.Button(
    button_frame,
    text="⏸ Pause",
    width=12,
    font=("Arial", 12)
)

pause_button.grid(
    row=0,
    column=1,
    padx=5
)


reset_button = tk.Button(
    button_frame,
    text="🔄 Reset",
    width=12,
    font=("Arial", 12)
)

reset_button.grid(
    row=0,
    column=2,
    padx=5
)


random_button = tk.Button(
    button_frame,
    text="🎲 Random",
    width=12,
    font=("Arial", 12)
)

random_button.grid(
    row=0,
    column=3,
    padx=5
)


# DRAW NUMBERS
def draw_numbers(
    highlight_indices=None,
    highlight_color="yellow",
    found_index=None,
    pivot_index=None
):

    canvas.delete("all")

    if highlight_indices is None:
        highlight_indices = []

    box_width = 85
    box_height = 85

    gap = 30

    total_width = (
        len(numbers) * box_width
        + (len(numbers) - 1) * gap
    )

    start_x = (
        1000 - total_width
    ) / 2

    y = 100

    for i, number in enumerate(numbers):

        x = (
            start_x
            + i * (box_width + gap)
        )

        color = "lightgray"

        # Current comparison
        if i in highlight_indices:
            color = highlight_color

        # Found element
        if found_index == i:
            color = "lightgreen"

        # Pivot
        if pivot_index == i:
            color = "orange"

        canvas.create_rectangle(
            x,
            y,
            x + box_width,
            y + box_height,
            fill=color,
            outline="black",
            width=2
        )

        canvas.create_text(
            x + box_width / 2,
            y + box_height / 2,
            text=str(number),
            font=("Arial", 20, "bold")
        )

        canvas.create_text(
            x + box_width / 2,
            y + box_height + 20,
            text=f"Index {i}",
            font=("Arial", 10)
        )


# RESET
def reset():

    global steps
    global current_step
    global running
    global paused
    global animation_id

    if animation_id is not None:

        root.after_cancel(
            animation_id
        )

        animation_id = None

    steps = []

    current_step = 0

    running = False

    paused = False

    pause_button.config(
        text="⏸ Pause"
    )

    status_label.config(
        text="Ready"
    )

    comparison_label.config(
        text="Operations: 0"
    )

    draw_numbers()


# START
def start():

    global steps
    global current_step
    global running
    global paused
    global target

    if running:
        return

    selected_name = (
        algorithm_var.get()
    )

    if selected_name not in algorithms:
        return

    algorithm = algorithms[
        selected_name
    ]

    # Search algorithms need target
    if algorithm.TYPE == "search":

        try:

            target = int(
                target_entry.get()
            )

        except ValueError:

            status_label.config(
                text="Invalid target"
            )

            return

        steps = algorithm.run(
            numbers,
            target
        )

    else:

        steps = algorithm.run(
            numbers
        )

    current_step = 0

    running = True

    paused = False

    pause_button.config(
        text="⏸ Pause"
    )

    status_label.config(
        text=f"Running {selected_name}..."
    )

    animate()


# ANIMATION
def animate():

    global current_step
    global running
    global animation_id

    if not running:
        return

    if paused:
        return

    if current_step >= len(steps):

        running = False

        status_label.config(
            text="Finished!"
        )

        return

    step = steps[
        current_step
    ]

    process_step(
        step
    )

    current_step += 1

    delay = speed_scale.get()

    animation_id = root.after(
        delay,
        animate
    )


# PROCESS STEP
def process_step(step):

    global numbers

    step_type = step["type"]

    # COMPARE
    if step_type == "compare":

        indices = []

        if "index" in step:

            indices.append(
                step["index"]
            )

            status_label.config(
                text=f"Checking index {step['index']}"
            )

        if "index1" in step:

            indices.append(
                step["index1"]
            )

        if "index2" in step:

            indices.append(
                step["index2"]
            )

        pivot = step.get(
            "pivot"
        )

        if pivot is not None:

            draw_numbers(
                highlight_indices=indices,
                highlight_color="yellow",
                pivot_index=pivot
            )

            status_label.config(
                text=f"Comparing with pivot at index {pivot}"
            )

        else:

            draw_numbers(
                highlight_indices=indices,
                highlight_color="yellow"
            )

        comparison_label.config(
            text=f"Operations: {current_step + 1}"
        )

    # SWAP
    elif step_type == "swap":

        numbers = step["array"].copy()

        draw_numbers(
            highlight_indices=[
                step["index1"],
                step["index2"]
            ],
            highlight_color="lightblue"
        )

        status_label.config(
            text=(
                f"Swap index "
                f"{step['index1']} and "
                f"{step['index2']}"
            )
        )

        comparison_label.config(
            text=f"Operations: {current_step + 1}"
        )

    # FOUND
    elif step_type == "found":

        draw_numbers(
            found_index=step["index"]
        )

        status_label.config(
            text=(
                f"✓ Found {target} "
                f"at index {step['index']}"
            )
        )

        comparison_label.config(
            text=f"Operations: {current_step + 1}"
        )

    # NOT FOUND
    elif step_type == "not_found":

        draw_numbers()

        status_label.config(
            text=f"✗ {target} was not found"
        )

    # FINISHED
    elif step_type == "finished":

        numbers = step["array"].copy()

        draw_numbers()

        status_label.config(
            text="✓ Sorting completed"
        )

        comparison_label.config(
            text=f"Operations: {current_step + 1}"
        )

# PAUSE / RESUME
def pause():

    global paused

    if not running:
        return

    paused = not paused

    if paused:

        pause_button.config(
            text="▶ Resume"
        )

        status_label.config(
            text="Paused"
        )

    else:

        pause_button.config(
            text="⏸ Pause"
        )

        status_label.config(
            text="Resuming..."

        )

        animate()


# RANDOM NUMBERS
def random_numbers():

    global numbers

    reset()

    numbers = random.sample(
        range(1, 100),
        8
    )

    draw_numbers()

    status_label.config(
        text="Random numbers generated"
    )


# CONNECT BUTTONS
start_button.config(
    command=start
)

pause_button.config(
    command=pause
)

reset_button.config(
    command=reset
)

random_button.config(
    command=random_numbers
)


# INITIAL DRAW
draw_numbers()


# START APPLICATION
root.mainloop()
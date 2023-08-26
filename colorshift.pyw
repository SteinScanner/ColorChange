import pygame
import sys
import tkinter as tk
from tkinter import ttk
import colorsys

# Initialize Pygame
pygame.init()

# Set up the display
window_size = (400, 400)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Color Shifting Window")

# Default settings
shift_speed = 1
shift_frequency = 100  # milliseconds
repeat_interval = 2000  # milliseconds
repeat_enabled = False

# Initialize color
hue = 0  # Start with red (0 degrees)

# GUI function to update settings
def update_settings():
    global shift_speed, shift_frequency, repeat_interval, repeat_enabled

    # Read values from the GUI
    shift_speed = int(speed_scale.get())
    shift_frequency = int(frequency_scale.get())
    repeat_interval = int(interval_scale.get())
    repeat_enabled = repeat_var.get()

    # Schedule the next update if repeating is enabled
    if repeat_enabled:
        window.after(repeat_interval, update_settings)

# Function to shift hue and update color
def shift_color():
    global hue, color

    # Shift the hue
    hue = (hue + shift_speed / 360.0) % 1.0  # Normalize hue to [0, 1]

    # Convert hue to RGB color
    color = tuple(int(c * 255) for c in colorsys.hsv_to_rgb(hue, 1, 1))

window = tk.Tk()
window.title("Color Shifting GUI")

speed_label = tk.Label(window, text="Shift Speed")
speed_label.pack()
speed_scale = ttk.Scale(window, from_=1, to=10, orient="horizontal")
speed_scale.set(shift_speed)
speed_scale.pack()

frequency_label = tk.Label(window, text="Shift Frequency (ms)")
frequency_label.pack()
frequency_scale = ttk.Scale(window, from_=10, to=1000, orient="horizontal")
frequency_scale.set(shift_frequency)
frequency_scale.pack()

interval_label = tk.Label(window, text="Repeat Interval (ms)")
interval_label.pack()
interval_scale = ttk.Scale(window, from_=100, to=5000, orient="horizontal")
interval_scale.set(repeat_interval)
interval_scale.pack()

repeat_var = tk.BooleanVar()
repeat_check = tk.Checkbutton(window, text="Repeat", variable=repeat_var)
repeat_check.pack()

update_button = tk.Button(window, text="Update Settings", command=update_settings)
update_button.pack()

# Main loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    shift_color()

    screen.fill(color)
    pygame.display.flip()

    # Control the speed of color shifting
    pygame.time.delay(shift_frequency)

    window.update()

pygame.quit()
sys.exit()

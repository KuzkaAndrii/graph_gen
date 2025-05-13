import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

root = tk.Tk()
root.title("Взаємодія з Matplotlib у Tkinter")

fig = Figure(figsize=(6, 4), dpi=100)
subplot = fig.add_subplot(111)
subplot.plot([1, 2, 3, 4], [5, 6, 7, 8])

canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

def on_mouse_click(event):
    x_data, y_data = subplot.transData.inverted().transform((event.x, event.y))
    print(f"Клік на графіку: x={x_data:.2f}, y={y_data:.2f}")

def on_mouse_motion(event):
    x_data, y_data = subplot.transData.inverted().transform((event.x, event.y))
    status_label.config(text=f"Координати: x={x_data:.2f}, y={y_data:.2f}")

def on_key_press(event):
    if event.char == 'r':
        subplot.cla()
        subplot.plot(np.random.rand(5), np.random.rand(5), 'o-')
        canvas.draw()

canvas_widget.bind("<Button-1>", on_mouse_click)
canvas_widget.bind("<Motion>", on_mouse_motion)
canvas_widget.bind("<Key>", on_key_press)
canvas_widget.focus_set()

status_label = tk.Label(root, text="Координати:")
status_label.pack(side=tk.BOTTOM)

def on_button_click():
    subplot.plot(np.random.rand(5), np.random.rand(5), 'o-')
    canvas.draw()

button = tk.Button(root, text="Оновити графік", command=on_button_click)
button.pack(side=tk.BOTTOM)

tk.mainloop()

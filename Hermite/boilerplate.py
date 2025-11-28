import matplotlib.pyplot as plt

# Persistent storage for clicked points
xs = []
ys = []

fig, ax = plt.subplots()
ax.set_title("Click to add points")
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Line/marker artist that we will update
points_plot, = ax.plot([], [], 'ro-', markersize=5)  # red dots connected by lines

def on_click(event):
    # Ignore clicks outside the axes
    if event.inaxes != ax:
        return

    # Left click: add point
    if event.button == 1:
        if event.xdata is None or event.ydata is None:
            return
        xs.append(event.xdata)
        ys.append(event.ydata)

        # Update plot data
        points_plot.set_data(xs, ys)
        fig.canvas.draw_idle()

    # Right click: clear all points (optional behavior)
    elif event.button == 3:
        xs.clear()
        ys.clear()
        points_plot.set_data([], [])
        fig.canvas.draw_idle()

# Connect the event handler
cid = fig.canvas.mpl_connect('button_press_event', on_click)

plt.show()

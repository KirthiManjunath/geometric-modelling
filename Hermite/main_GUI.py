import matplotlib.pyplot as plt
import Hermite as h
import numpy as np

points = []
tangents = []
X = []
Y = []
hx = []
hy = []
X_curve = []
Y_curve = []

fig, ax = plt.subplots()
ax.set_title("Click to add points")
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

points_plot, = ax.plot([], [], 'ro', markersize=5)  
curve_plot, = ax.plot([], [], 'b', linewidth=1)
#tangents_plot, = ax.plot([], [], 'g--', linewidth=0.5)

def on_click(event):
    if event.inaxes != ax:
        return
    
    if event.button == 1:
        if event.xdata is None or event.ydata is None:
            return
        X.append(event.xdata)
        Y.append(event.ydata)

        points.append( (X[-1], Y[-1]) )
        if len(X) == 2:
            tangents.append(points.pop(-1))

        if len(X) == 4:
            tangents.append(points.pop(-1))

        if len(X) >= 2 and len(tangents) >= 2:
            if len(hx) == 0:
                X.pop(3)
                Y.pop(3)
                X.pop(1)
                Y.pop(1)

            hx.append(h.hermite(X[-1], tangents[-1][0], X[-2], tangents[-2][0]))
            hy.append(h.hermite(Y[-1], tangents[-1][1], Y[-2], tangents[-2][1]))
            X_curve.append(hx[-1].hermite_basis())
            Y_curve.append(hy[-1].hermite_basis())

            points_plot.set_data(X, Y)
            curve_plot.set_data(np.concatenate(X_curve), np.concatenate(Y_curve))
            fig.canvas.draw_idle()

    elif event.button == 3:
        X.clear()
        Y.clear()
        points.clear()
        tangents.clear()
        hx.clear()
        hy.clear()
        X_curve.clear()
        Y_curve.clear()
        points_plot.set_data([], [])
        curve_plot.set_data([], [])
        #tangents_plot.set_data([], [])
        fig.canvas.draw_idle()

# Connect the event handler
cid = fig.canvas.mpl_connect('button_press_event', on_click)
plt.show()

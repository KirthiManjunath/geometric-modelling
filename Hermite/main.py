import matplotlib.pyplot as plt
import Hermite as h
import numpy as np
#from matplotlib.widgets import Button

points = []
tangents = []
colors = plt.cm.tab10.colors

try:
    x1, y1 = map(int, input("Enter first point (x1 y1): ").split())
except:
    print("Invalid input. Please enter two integers separated by a space.")
    x1, y1 = map(int, input("Enter first point (x1 y1): ").split())
try:
    x2, y2 = map(int, input("Enter second point (x2 y2): ").split())
except:
    print("Invalid input. Please enter two integers separated by a space.")
    x2,y2 = map(int, input("Enter second point: ").split())
try:
    (xt1,yt1) = map(int, input("Enter first tangent: ").split())
except:
    print("Invalid input. Please enter two integers separated by a space.")
    (xt1,yt1) = map(int, input("Enter first tangent: ").split())
try:
    (xt2,yt2) = map(int, input("Enter second tnagent: ").split())
except:
    print("Invalid input. Please enter two integers separated by a space.")
    (xt2,yt2) = map(int, input("Enter second tangent: ").split())

points.append( (x1,y1) )
points.append( (x2,y2) )
tangents.append( (xt1,yt1) )
tangents.append( (xt2,yt2) )

hx = []
hy = []
hx.append(h.hermite(x2, xt2, x1, xt1))
hy.append(h.hermite(y2, yt2, y1, yt1))
more = True

X = hx[0].hermite_basis()
Y = hy[0].hermite_basis()

plt.figure()
plt.plot(X,Y)
plt.plot(points[0][0], points[0][1], 'ro', markersize = 0.5)  # first point
plt.plot(points[1][0], points[1][1], 'ro', markersize = 0.5)  #  
plt.plot([x1, x1 + xt1], [y1, y1 + yt1], 'b--', linewidth = 0.5)
plt.plot([x2, x2 + xt2], [y2, y2 + yt2], 'b--', linewidth = 0.5)
plt.title("Hermite Curve")
plt.show()
i = 0

while more:
    # ask explicitly for a yes/no response; any non-yes will stop
    response = input("Add another point? [y/N]: ").strip().lower()
    if response not in ("y", "yes", 1):
        break
    i += 1
    try:
        (x,y) = map(int, input("Enter next point: ").split())
    except:
        print("Invalid input. Please enter two integers separated by a space.")
        (x,y) = map(int, input("Enter next point: ").split())
    points.append( (x,y) )
    hx.append(h.hermite(x, prev = hx[i-1]))
    hy.append(h.hermite(y, prev = hy[i-1]))
    tangents.append((hx[i].m1, hy[i].m1))
    for j in range (len(hx)):
        plt.plot(hx[j].hermite_basis(), hy[j].hermite_basis(), color = colors[j])
    for j in range(len(points)):
        plt.plot(points[j][0], points[j][1], 'ro', markersize = 0.5)  
        if j < len(tangents):
            plt.plot([points[j][0], points[j][0] + tangents[j][0]], [points[j][1], points[j][1] + tangents[j][1]], 'b--', linewidth = 0.5)

    newX = np.array(hx[i].hermite_basis())
    newY = np.array(hy[i].hermite_basis())
    X = np.concatenate((X, newX))
    Y = np.concatenate((Y, newY))
    #plt.plot(X,Y, color = 'black')
    plt.title("Hermite Curve")
    plt.show()

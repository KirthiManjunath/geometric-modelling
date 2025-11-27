import matplotlib.pyplot as plt
import Hermite as h
import numpy as np

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
hx = []
hy = []
hx.append(h.hermite(x2, xt2, x1, xt1))
hy.append(h.hermite(y2, yt2, y1, yt1))
more = True

X = hx[0].hermite_basis()
Y = hy[0].hermite_basis()

plt.plot(X,Y)
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
    hx.append(h.hermite(x, prev = hx[i-1]))
    hy.append(h.hermite(y, prev = hy[i-1]))

    newX = np.array(hx[i].hermite_basis())
    newY = np.array(hy[i].hermite_basis())
    X = np.concatenate((X, newX))
    Y = np.concatenate((Y, newY))
    plt.plot(X,Y)
    plt.title("Hermite Curve")
    plt.show()

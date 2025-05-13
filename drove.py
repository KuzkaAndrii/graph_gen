import matplotlib.pyplot as plt
import numpy as np
from math import pi
def norm(x1, y1, x2, y2):
    v1=x2-x1
    v2=y2-y1
    v1, v2=v2, -1*v1
    v1, v2=v1/(10*(v1**2+v2**2)**0.5), v2/(10*(v1**2+v2**2)**0.5)
    return v1, v2
def petl(x, y, n, draw_1, draw_2):
    lx=np.random.rand(3)
    print(1)
    ly=(np.array([1.0, 1.0, 1.0])-lx**2)**0.5
    print(2)
    lx, ly=0.1*lx, 0.1*ly
    print(3)
    lx[2], ly[2] = x, y
    print(4)
    draw_1.plot(lx, ly, color='black')
    draw_2.draw()
    return


def edge(x1, y1, x2, y2, n, draw_1, draw_2):
    v1, v2 = norm(x1, y1, x2, y2)
    x, y=(x1+x2)/2+v1*n, (y1+y2)/2+v2*n

    draw_1.plot(np.linspace(x1, x, 100), np.linspace(y1, y, 100), color='black')
    draw_2.draw()
    draw_1.plot(np.linspace(x, x2, 100), np.linspace(y, y2, 100),  color='black')
    draw_2.draw()
    return
if __name__=="__main__":
    print("Hello, World!")
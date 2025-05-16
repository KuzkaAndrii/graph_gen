#завантажені бібліотеки
import numpy as np


# Вектор між 2 точками
def norm(x1, y1, x2, y2):
    v1=x2-x1
    v2=y2-y1
    v1, v2=v2, -1*v1
    v1, v2=v1/(10*(v1**2+v2**2)**0.5), v2/(10*(v1**2+v2**2)**0.5)
    return v1, v2


# Петля
def petl(x, y, n, draw_1, draw_2):
    lx=np.random.rand(4)

    ly=((-1)**n)*(np.array([1.0, 1.0, 1.0, 1.0])-lx**2)**0.5

    lx, ly=00.1*lx, 00.1*ly

    lx[3], ly[3] = x, y
    lx[0], ly[0] = x, y

    draw_1.plot(lx, ly, color='black')
    draw_2.draw()
    return


# Ребро
def edge(x1, y1, x2, y2, n, draw_1, draw_2, col='black'):
    v1, v2 = norm(x1, y1, x2, y2)
    x, y=(x1+x2)/2+v1*n, (y1+y2)/2+v2*n

    draw_1.plot(np.linspace(x1, x, 100), np.linspace(y1, y, 100), color=col)
    draw_2.draw()
    draw_1.plot(np.linspace(x, x2, 100), np.linspace(y, y2, 100),  color=col)
    draw_2.draw()
    return


# орієнтоване ребро
def edge_arr(x1, y1, x2, y2, n, draw_1, draw_2):
    v1, v2 = norm(x1, y1, x2, y2)
    x, y = (x1 + x2) / 2 + v1 * n, (y1 + y2) / 2 + v2 * n

    draw_1.plot(np.linspace(x1, x, 100), np.linspace(y1, y, 100), color='black')
    draw_2.draw()
    draw_1.arrow(x, y, x2-x, y2-y, color='black', fc='black', ec='black', head_width=0.5, head_length=0.5, length_includes_head=True)
    draw_2.draw()
    return


# орієньована петля
def petl_arr(x, y, n, draw_1, draw_2):
    lx=np.random.rand(3)

    ly=((-1)**n)*(np.array([1.0, 1.0, 1.0])-lx**2)**0.5

    lx, ly=0.01*lx, 0.01*ly

    lx[2], ly[2] = x, y

    draw_1.plot(lx, ly, color='black')
    draw_1.arrow(lx[1], ly[1], lx[2]-lx[1], ly[2]-ly[1], color='black', fc='black', ec='black', head_width=0.5, head_length=0.5, length_includes_head=True)
    draw_2.draw()
    return
if __name__=="__main__":
    print("Hello, World!")
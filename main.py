import numpy as np
from numpy.linalg import norm


def euler_method(t0, T, h0, Nx, eps, func, y0):
    """Модифицированный метод Эйлера для решения задачи Коши систем ОДУ"""

    def euler_method_step(t0, y0, h):
        """Вычисление значения вектор-функции в точке t0 + h"""
        # Найти значение вектор-функции в средней точке t0 + h/2
        y1 = y0 + h/2 * func(t0, y0, counter)
        # Найти значение вектор-функции в конечной узловой точке t0 + h
        y2 = y0 + h * func(t0 + h/2, y1, counter)
        return y2

    t = t0
    y = y0
    h = h0
    counter = [0]

    print(f"{t:13.6f}{h:13.6f}{0:13.5e}{counter[0]:13d}", *[f"{x:12.6f}" for x in y])

    while t < T and counter[0] < Nx:
        # Найти приближенное значение y_k с шагом h
        y1 = euler_method_step(t, y, h)

        # Найти приближенное значение y_k с шагом h/2
        y2 = euler_method_step(t, y, h/2)
        y2 = euler_method_step(t+h/2, y2, h/2)

        # Вычислить поправку Рунге
        R = norm(y1 - y2) / 3

        if R > eps:
            h /= 2
            continue

        if R < eps / 64:
            h *= 2

        t += h
        y = y1

        print(f"{t:13.6f}{h:13.6f}{R:13.5e}{counter[0]:13d}", *[f"{x:12.6f}" for x in y])


t_0 = float(input())
T = float(input())
h_0 = float(input())
N_x = int(input())
eps = float(input())
n = int(input())
function_code = []
for i in range(n+3):
    line = input()
    function_code.append(line)

# Создание функции
function_definition = "\n".join(function_code)
exec(function_definition)

input_string = input()
initial_conditions = [int(x) for x in input_string.split()]

euler_method(t_0, T, h_0, N_x, eps, fs, initial_conditions)
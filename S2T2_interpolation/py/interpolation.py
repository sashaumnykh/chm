import numpy as np


def func(x):
    """
    Целевая функция (векторизованная): должна принимать линейный массив и возвращать линейный массив
    """
    return np.exp(np.cos(x))


def interpol(xs, ys):
    """
    Полиномиальная интерполяция по X и Y. Нужно вернуть коэффициенты интерполяционного многочлена
    """
    return np.polyfit(xs, ys, len(xs) - 1)

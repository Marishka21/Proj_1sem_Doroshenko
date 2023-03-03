"""Вычисление периметра и площади окружности"""

__all__ = ['circle_area', 'circle_perimeter']

from math import pi
default_radius = 5


def circle_perimeter(r=default_radius):
    """Эта функция вычисляет периметр окружности"""
    return 2 * pi * r


def circle_area(r=default_radius):
    """Эта функция вычисляет площадь окружности"""
    return pi * r ** 2
"""Вычисление периметра и площади треугольника"""

__all__ = ['triangle_perimeter', 'triangle_area']

from math import sqrt
a = 7
b = 2
c = 8


def triangle_perimeter(x1=a, x2=b, x3=c):
    """Вычисление периметра треугольника"""
    return x1 + x2 + x3


def triangle_area(x1=a, x2=b, x3=c):
    """Вычисление площади треугольника"""
    p = (x1 + x2 + x3) / 2
    return sqrt(p * (p - x1) * (p - x2) * (p - x3))
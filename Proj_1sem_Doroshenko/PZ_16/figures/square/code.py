"""Вычисление периметра и площади квадрата"""

__all__ = ['square_area', 'square_perimeter']

a = 15


def square_perimeter(x=a):
    """Вычисление периметра квадрата"""
    return 4 * x


def square_area(x=a):
    """Вычисление площади квадрата"""
    return x ** 2


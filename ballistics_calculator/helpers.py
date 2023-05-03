"""
Предоставляет вспомогательные функции для работы с баллистикой.
"""
import math


def get_radians(degrees: float) -> float:
    """
    Получение радианов из градусов.

    :param degrees: Градусы
    :type degrees: float
    :return: Радианы
    :rtype: float
    """
    return math.radians(degrees)
"""
Предоставляет основный класс Ballistic для работы с расчетами.
"""
import math
import numpy as np
import matplotlib.pyplot as plt


class Ballistic:
    """Класс балисстики"""

    alpha: float
    boost: float
    g: float
    _flight_time: float = None
    _distance: float = None
    _max_height: float = None

    def __init__(
            self,
            alpha: float,
            boost: float,
            g: float = 9.8,
    ):
        """
        Инициализация

        :param alpha: Угол наклона
        :type alpha: float
        :param boost: Ускорение
        :type boost: float
        :param g: Сила притяжения. По-умолчанию 9.8
        :type g: float | None
        """
        self.alpha = alpha
        self.boost = boost
        self.g = g

    @property
    def distance(self) -> float:
        """
        Максимальное расстояние, на которое улетит объект.

        Максимальное расстояние высчитывается по формуле: V0 * cos(alpha) * t

        :return: Расстояние
        :rtype: float
        """
        if self._distance is None:
            self._distance = self.boost * math.cos(self.alpha) * self.flight_time
        return self._distance

    @property
    def flight_time(self) -> float:
        """
        Время полета объекта.

        Время полета высчитывается по формуле: 2 * V0 * sin(alpha) / g

        :return: Время полета
        :rtype: float
        """
        if self._flight_time is None:
            self._flight_time = 2 * self.boost * math.sin(self.alpha) / self.g
        return self._flight_time

    @property
    def max_height(self) -> float:
        """
        Максимальная высота, на которую поднимется объект.

        Высота высчитаывается по формуле: V0 * cos(alpha) / 2 * t

        :return: Максимальная высота
        :rtype: float
        """
        if self._max_height is None:
            self._max_height = self.boost * math.cos(self.alpha) / 2 * self.flight_time
        return self._max_height

    def show_plot(self, title: str, need_grid: bool = True) -> None:
        """
        Показать полученый график траектории.

        Траектория строится по формуле:
        y = x * tg(x) - (g * x ^ 2) / (2 * V0 ^ 2 * cos(alpha) ^ 2)

        :param title: Название графика
        :type title: str
        :param need_grid: Нужна ли сетка на графике
        :type need_grid: bool
        """
        x = np.arange(0, self.distance, 0.01)
        y = (
            math.tan(self.alpha) * x -
            self.g * x ** 2 / (2 * self.boost ** 2 * math.cos(self.alpha) ** 2)
        )
        plt.plot(x, y)
        plt.xlabel(r"$x$")
        plt.ylabel(r"$f(x)$")
        plt.title(title)
        plt.grid(need_grid)
        plt.show()

# ballistics-calculator

Эта библиотека содержит функции для расчета баллистики.

### О проекте

Балистика - это наука, изучающая движение тел в воздухе или в вакууме под
воздействием силы тяжести и других сил. В широком смысле, балистика охватывает 
все аспекты движения тел, включая их траектории, скорости и энергию, 
а также их взаимодействие с окружающей средой. Балистика применяется 
в различных областях, включая военную технику, спортивную стрельбу, 
астрономию и космические исследования.

### Установка

``` $ pip install -e git+https://github.com/timursungatullin/ballistics-calculator.git#egg=ballistics_calculator ```


### Использование

```python
from ballistics_calculator import Ballistic, get_radians

V0 = 10                             # Начальное ускорение
alpha = 45                          # Угол наклона в градусах, можно сразу использовать радианы
alpha_radians = get_radians(alpha)  # Угол наклона в радианах
G = 9.80665                         # Сила притяжение
calc = Ballistic(alpha_radians, V0, G)
print(f"Расстояние:          {calc.distance}")
print(f"Время полета:        {calc.flight_time}")
print(f"Максимальная высота: {calc.max_height}")
calc.show_plot(title="Задача 1")
```
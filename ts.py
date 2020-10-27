# %% [markdown]
# # Кидаем камень
#
# ## Подготовка
#
# Добавим все библиотеки, которые мы будем использовать в окружение.

# %%
from ipycanvas import Canvas  # Канва для отображения действий
import ipywidgets as wg  # Виджеты для интерактива

import typing  # Строгая типизация

import math  # Математические формулы

import numpy as np # Работа с векторами

# %% [markdown]
# Для начала создаем канву и метод, с помощью которого мы будем рисовать положения тела в пространстве после его броска нами.
#
# В данном случае будем использовать черный прямоугольный камень. Сопротивлением воздуха пренебречь

# %%
width = 1024
height = 256

# Канва
canvas = Canvas(width=width, height=height)

stone_color = "black"
angle_line_color = "blue"

# %% [markdown]
# Создадим так же несколько методов для рисования нужных нам примитивов

# %%


def clear_canvas():
    """Очистка канвы"""
    global canvas

    canvas = Canvas(width=width, height=height)
    canvas.clear()


def connect_two_point(start: typing.List[float], end: typing.List[float], color: str):
    """Линия между двумя точками"""
    global canvas

    canvas.move_to(start[0], start[1])
    canvas.line_to(end[0], end[1])
    canvas.stroke_style = color
    canvas.stroke()


def fill_rect(position: typing.List[float], size: typing.List[float], color: str):
    global canvas

    canvas.fill_style = color
    canvas.fill_rect(position[0], position[1], size[0], size[1])


def draw_point(position: typing.List[float]):
    """Рисуем камень"""
    size = np.array([10, 10])
    fill_rect(position, size, stone_color)


def draw_line(angle):
    """Отрисовка линии угла броска"""
    start = np.array([0, height])
    rad_angle = math.radians(angle)
    end = np.array([
        math.cos(rad_angle) * min(width, height),  # Линия видна по всей канве
        # Система отсчета канвы - от верхнего левого угла, удобнее - од нижнего левого => переворачиваеем (height - y)
        height - math.sin(rad_angle) * height
    ])
    clear_canvas()
    connect_two_point(start, end, angle_line_color)

# %% [markdown]
# ## Математическая составляющая
#
# Мы будем считать положение тела по формуле $\vec{P}(t) = \vec{P_0} + \vec{V_0}t + \frac{\vec{a}t^2}{2}$, где:
# - $P$ - положение тела в текущий момент
# - $P_0$ - начальное положение тела
# - $V_0$ - начальная скорость
# - $a$ - ускорение тела
# - $t$ - время прошедшее с момента броска

# %%


def next_position(start_position: np.ndarray, start_velocity: np.ndarray, acceleration: np.ndarray):
    """Функция с замыканием для рассчета следующего положения в зависимости от аргументов и времени"""
    def future_position(t: float) -> np.ndarray:
        return start_position + (start_velocity * t) + (acceleration * (t ** 2.0)) / 2.0

    return future_position

# %% [markdown]
# ### Задание начальных условий
#
# Для начала положим, что мы начинаем движение из точки $P_0(0;0)$ со скоростью ```k_velocity``` метров в секунду и углом ```start_angle``` радиан


# %%
g = np.array([0, -9.81])  # Ускорение свободного падения (направлено вниз)

position = np.array([0, 0])

full_time = 60  # Cколько будем просчитывать (в секундах)


def show_line(angle, delta_time, force):
    draw_line(angle)

    rad_angle = math.radians(angle)

    start_velocity = np.array(
        [math.cos(rad_angle), math.sin(rad_angle)]) * force

    func = next_position(position, start_velocity, g)

    slices = [func(float(i) * delta_time)
              for i in range(0, int(full_time / delta_time))]

    for i in slices:
        draw_point([i[0], height - i[1]])

    return canvas


start_angle_w = wg.FloatSlider(
    description="Угол броска", min=0, max=90, step=0.5)
# Через какой отрезок времени будем делать срезы объекта
delta_time_w = wg.FloatSlider(
    description="Дельта времени", min=0.1, max=4, step=0.5)
force_w = wg.FloatSlider(
    description="Сила, с которой кидаем камень", min=0.0, max=100.0, step=0.5)

_ = wg.interact(show_line, angle=start_angle_w,
                delta_time=delta_time_w, force=force_w)

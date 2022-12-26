import math
from random import random

import numpy as np
from scipy.stats import t

import pandas as pd

def write_file(path,x,y,y1): #сохранение в файл

    dict = {'x': x,
            'y': y,
            'y1': y1
            }

    dataframe = pd.DataFrame(dict)
    dataframe.to_csv(path, index=False)  # при сохранении файла отбросить индекс

def read_file(path): #чтение из файла
    dataframe = pd.read_csv(path)
    x = np.array(dataframe.x.to_list())
    y = np.array(dataframe.y.to_list())
    y1 = np.array(dataframe.y1.to_list())
    return x, y, y1

def genDate(f,x,a,b,c=0): #портим данные (на вход номер функции и передаваемые параметры)
    y = np.empty(len(x))
    match f: #в зависимости от номера создаем теоретические(правильные) данные
        case 1:
            y = a * x + b
        case 2:
            y = a * x**2 + b*x + c
        case 3:
            y = a * np.log(x) + b
    y1 = np.empty(len(x))
    for i in range(len(x)): #портим данные
        y1[i] = y[i] + 4 * random()-2
    return y, y1

def line(x, y1): #линейная регрессия

    x2 = x**2
    xy = x * y1
    n = len(x)
    matr = np.matrix([[x2.sum(), x.sum()],
                      [x.sum(), n]])  # матрица левой части системы уравнений
    matr1 = np.matrix([[xy.sum(), x.sum()],
                       [y1.sum(), n]])  # матрица для а
    matr2 = np.matrix([[x2.sum(), xy.sum()],
                       [x.sum(), y1.sum()]])  # матрица для b
    main_det = np.linalg.det(matr)
    # считаем определители и применяем метод Крамера
    det1 = np.linalg.det(matr1)
    det2 = np.linalg.det(matr2)
    a1 = det1 / main_det
    b1 = det2 / main_det
    y2 = a1 * x + b1
    print(f'a1={a1}\nb1={b1}\n')
    return a1,b1,y2

def parabola(x,y1): #параболла
    x4 = x ** 4
    x3 = x ** 3
    x2 = x ** 2
    yx2 = y1 * x2
    yx = y1 * x
    n = len(x)
    matr = np.matrix([[x4.sum(), x3.sum(), x2.sum()],
                      [x3.sum(), x2.sum(), x.sum()],
                      [x2.sum(), x.sum(), n]])  # матрица левой части системы уравнений
    matr1 = np.matrix([[yx2.sum(), x3.sum(), x2.sum()],
                       [yx.sum(), x2.sum(), x.sum()],
                       [y1.sum(), x.sum(), n]])  # матрица для а
    matr2 = np.matrix([[x4.sum(), yx2.sum(), x2.sum()],
                       [x3.sum(), yx.sum(), x.sum()],
                       [x2.sum(), y1.sum(), n]])  # матрица для b
    matr3 = np.matrix([[x4.sum(), x3.sum(), yx2.sum()],
                       [x3.sum(), x2.sum(), yx.sum()],
                       [x2.sum(), x.sum(), y1.sum()]])  # матрица для c
    #считаем определители и применяем метод Крамера
    det = np.linalg.det(matr)
    det1 = np.linalg.det(matr1)
    det2 = np.linalg.det(matr2)
    det3 = np.linalg.det(matr3)
    a1 = det1 / det
    b1 = det2 / det
    c1 = det3 / det
    y2 = a1 * x ** 2 + b1 * x + c1
    print(f'a1={a1}\nb1={b1}\nc1={c1}')
    return a1, b1, c1, y2

def log(x,y1): #логариф
    t = np.empty(len(x))
    for i in range(len(x)):
        t[i] = math.log(x[i])
    a1,b1,y2 = line(t,y1) #считаем как линейную регрессию
    return a1,b1,y2

def hallway(x,n,s,y2): # коридор
    Sost = math.sqrt(s / (n - 2))
    x_mean = np.mean(x) #среднее
    sigma = np.var(x) #дисперсия
    ta = t.ppf(0.9, df=n - 2) #значение распределения Стьюдента
    print(ta)
    yk1 = np.empty(n) #нижняя граница
    yk2 = np.empty(n) #верхняя граница
    for i in range(n):
        m = Sost * math.sqrt(1+ (1 / n) + ((x[i] - x_mean) ** 2) / (n * sigma)) #считаем m
        yk1[i] = y2[i] - ta * m #нижняя граница
        yk2[i] = y2[i] + ta * m #верхняя граница
    return yk1, yk2


def m(s,n,x): #m для оценки параметра
    Sost = math.sqrt(s / (n - 2))
    sigma = math.sqrt(np.var(x))
    alpha = 0.1
    ta = t.ppf(1 - alpha / 2, df=n - 2)
    m = (Sost*math.sqrt((x**2).sum()))/(sigma*n)
    return ta*m




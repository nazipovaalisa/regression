import numpy as np
import calc
import matplotlib.pyplot as plt

x = np.arange(1,10,0.3)
a = 2
b = -3
c = 3
path1 = "line.csv"
path2 = "parabola.csv"
path3 = "log.csv"

y = np.empty(len(x))
y1 = np.empty(len(x))
y2 = np.empty(len(x))

func = 1 #здесь надо менять цифры от 1 до 3 чтобы запустить функцию
match (func):
    case 1: #линейная функция
        y,y1 = calc.genDate(1,x,a,b)
        calc.write_file(path1,x,y,y1)
        x,y,y1 = calc.read_file(path1)
        a1, b1, y2 = calc.line(x, y1)
    case 2: #параболла
        y,y1 = calc.genDate(2,x,a,b,c)
        calc.write_file(path2,x,y,y1)
        x,y,y1 = calc.read_file(path2)
        a1, b1, c1, y2 = calc.parabola(x,y1)
    case 3: #логарифм
        y, y1 = calc.genDate(3, x, a, b)
        calc.write_file(path3, x, y, y1)
        x, y, y1 = calc.read_file(path3)
        a1, b1, y2 = calc.log(x, y1)

print(x)
print(y1)

s = ((y1 - y2) ** 2).sum() #функция, которую надо минимизировать
print(f's={s}')
yk1, yk2 = calc.hallway(x, len(x), s, y2) #коридор

plt.plot(x, y, color='blue', label='y - теоретические')
plt.scatter(x, y1, marker='.', c='green', label='y - экспериментальные')
plt.plot(x, y2, color='red', label='прогноз')
plt.plot(x, yk1, color='black', linestyle='--', label='коридор')
plt.plot(x, yk2, color='black', linestyle='--')
plt.grid()
plt.legend()
plt.show()








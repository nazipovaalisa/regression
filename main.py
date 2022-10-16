import numpy as np
import calc
import matplotlib.pyplot as plt

x = np.arange(1,11,0.3)
# a = 2
# b = 3
a = 2
b = -6
c = 5
path1 = "line.csv"
path2 = "parabola.csv"
path3 = "log.csv"

#линейная функция

# y,y1 = calc.genDate(1,x,a,b)
# calc.write_file(path1,x,y,y1)
# x,y,y1 = calc.read_file(path1)
# a1, b1, y2 = calc.line(x, y1)

#парабола

# y,y1 = calc.genDate(2,x,a,b,c)
# calc.write_file(path2,x,y,y1)
# x,y,y1 = calc.read_file(path2)
# a1, b1, c1, y2 = calc.parabola(x,y1)

# логарифм

y,y1 = calc.genDate(3,x,a,b)
calc.write_file(path3,x,y,y1)
x,y,y1 = calc.read_file(path3)
a1,b1,y2 = calc.log(x,y1)

print(x)
print(y1)


s = ((y1 - y2) ** 2).sum()
print(f's={s}')
yk1, yk2 = calc.hallway(x, len(x), s, y2)

print(yk1)
#
# print(f'Стандартная ошибка a1:\n({a1 - calc.m(s,len(x),x)}, {a1 + calc.m(s,len(x),x)})')
# print(f'Стандартная ошибка b1:\n({b1 - calc.m(s,len(x),x)}, {b1 + calc.m(s,len(x),x)})')
# print(f'Стандартная ошибка c1:\n({c1 - calc.m(s,len(x),x,c1)}, {c1 + calc.m(s,len(x),x,c1)})')

plt.plot(x, y, color='black', label='y - теоретические')
plt.scatter(x, y1, marker='*', c='black', label='y - экспериментальные')
plt.plot(x, y2, color='red', label='прогноз')
plt.plot(x, yk1, color='blue', linestyle='--', label='коридор')
plt.plot(x, yk2, color='blue', linestyle='--')
plt.grid()
plt.legend()
plt.show()








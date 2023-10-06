from math import sqrt

one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]
print('Максимальная сторона в первом списке', sorted(one, reverse=True)[:1])
print('Максимальная сторона в втором списке', sorted(two, reverse=True)[:1])
print('Максимальная сторона в третьем списке', sorted(three, reverse=True)[:1])
print('Минимальная сторона в первом списке', sorted(one)[:1])
print('Минимальная сторона в втором списке', sorted(two)[:1])
print('Минимальная сторона в третьем списке', sorted(three)[:1])
a1 = sorted(one, reverse=True)[:1]
b1 = sorted(two, reverse=True)[:1]
c1 = sorted(three, reverse=True)[:1]
a11 = a1[0]
b11 = b1[0]
c11 = c1[0]
p1 = (a11 + b11 + c11) / 2
area1 = sqrt(p1 * (p1 - a11) * (p1 - b11) * (p1 - c11))
print('Площадь большого треугольника', area1)
a2 = sorted(one)[:1]
b2 = sorted(two)[:1]
c2 = sorted(three)[:1]
a22 = a1[0]
b22 = b1[0]
c22 = c1[0]
p2 = (a22 + b22 + c22) / 2
area2 = sqrt(p2 * (p2 - a22) * (p2 - b22) * (p2 - c22))
print('Площадь маленького треугольника', area2)

from math import sqrt


def date(a, b, c):
    p = (a + b + c) / 2
    geron = sqrt(p * (p - a) * (p - b) * (p - c))
    return geron

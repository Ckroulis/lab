def date(*args):
    sr = 0
    for i in args:
        sr += i
    print(sr / len(args))


if __name__ == '__main__':
    date(2, 2, 3, 4, 5, 6, 7)

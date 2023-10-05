from random import randint


def ran(r):
    if r == 5 or r == 6:
        print('Вы победили')
    elif r == 3 or r == 4:
        ran(r)
    else:
        print('Вы проиграли')


if __name__ == '__main__':
    r: int = randint(1, 6)
    ran(r)

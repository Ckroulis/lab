class TailNotFoundException(Exception):
    pass
def find_cat_tail(cat):
    if 'хвост' not in cat:
        raise TailNotFoundException("У кошки нет хвоста")
    else:
        return cat['хвост']

cat1 = {'Имя': 'Кискисыч', 'Цвет': 'Серый'}
try:
    tail = find_cat_tail(cat1)
    print(f"{cat1['Имя']} длина хвоста: {tail}")
except TailNotFoundException as e:
    print(e)
def measure_tail_length(cat):
    try:
        tail = find_cat_tail(cat)
        length = len(tail)
        print(f"{cat['Имя']} длина хвоста: {length} cm")
    except TailNotFoundException as e:
        print(e)

cat2 = {'Имя': 'Пушистик', 'Цвет': 'Ораньжевый'}
measure_tail_length(cat1)

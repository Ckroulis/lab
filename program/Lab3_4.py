a = str(input())
count: int = 0
glas = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u', 'Y', 'y']
print(len(a))
print(a.lower())
for i in a:
    if i in glas:
        count += 1
print('Голичество гласнных ', count)
print(a.replace("ugly", "beauty"))
print(a.startswith('The'))
print(a.endswith('end'))

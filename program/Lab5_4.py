dnev1 = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
dnev2 = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
dnev3 = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]
dnev11 = [4 if i == 3 else i for i in dnev1 if i != 2]
dnev22 = [4 if i == 3 else i for i in dnev2 if i != 2]
dnev33 = [4 if i == 3 else i for i in dnev3 if i != 2]
print(dnev11)
print(dnev22)
print(dnev33)

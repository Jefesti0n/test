# n = input()
# new_n = int(n[:-5] + n[-5:][::-1])
#
# print(new_n)
# print(n[:-5],           #знаки от начала до -5 невключительно - 1) если 6 знаков - будет напечатан первый символ 2) если 5 - не будет никакого (?)
#       n[-5:],           #1) от 2 знака до конца
#       n[::-1],          #задом наперёд
#       n[-5:][::-1])     #от 2 знака до конца, но задом наперёд - то есть, сначала создаём срез в первых [], затем делаем его срез во вторых []


# план:
# 1)Перевернуть строку
# 2)через каждые 3 символа вставить запятую
# - надо чтобы последним символом не была запятая
# - решить циклом for??
# 3)перевернуть обратно
# 000, 000, 123, - проблема чисел, количество символов которых кратно трём
# n = 1_312_332
# reverse = 233_213_1


n = list(input())
n = n[::-1]
print(n)
for i in range(3, len(n), 3):
    n.insert(i, ",")

print(insert(n))
n = (n[::-1])
n = ''.join(n)
print(n)





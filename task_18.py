# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

n= int(input("Введите число элементов в массиве: "))
array = []
for i in range(n):                                                      # построчно вносим значения в список
    array.append(int(input(f"Введите число {i} массива: ")))
x= int(input("Введите значение для поиска: "))
min_namber=x-array[0]
index=0
for j in range(n):                                                      # проверяем элементы массива на близость к числу Х
    a=x-array[j]
    if a<0:                                                             # Если Х оказалось меньше искомого числа 
        a=-a
    if min_namber > a:                                                  # Проверяем, ближе проверяемое число к Х, чем ранее проверенные
        min_namber=a
        index=j

print(array[index])

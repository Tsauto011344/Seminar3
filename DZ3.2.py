import random
n = int(input('Введите размер массива: '))
x = int(input('Введите искомое число x: '))
arr = []
for i in range(n):
    arr.append(random.randrange(n))
print(arr)
def nearval(arr, number):
    return min(arr, key=lambda x: abs(number - abs(x))) 
print(f'Ближайшее к {x} число в массиве: {nearval(arr, x)}')
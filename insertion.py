# Сортировка вставками
# Сортировка вставками работает путем последовательного перемещения элементов массива,
# вставляя каждый элемент на его правильное место в уже отсортированной части массива.

# Чтобы выполнить сортировку вставки:
# - начинаем сортировку со второго элемента списка, так как первый элемент уже считается отсортированным;
# - текущий элемент, выбранный на каждом шаге цикла, сохраняется в переменной key;
# - сравниваем текущий элемент key с элементами слева от него;
# - все элементы, которые больше чем key, сдвигаются вправо;
# - после сдвига всех элементов, которые больше чем key, вправо, вставляем key на освобожденное место;
# - повторяем описанный процесс для каждого элемента списка.

a = [-3, 5, 0, -9, 1, 100, 10]


def insert_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


insert_sort(a)
print(a)

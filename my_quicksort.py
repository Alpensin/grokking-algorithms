# Worst O(n^^2)
# Avg O(nlogn)
# Best O(nlogn)
# При nlogn быстрее сортировки слиянием, т.к. меньше константа
import random
import timeit


def qsort_first(array):
    """Вариант, когда опорным выбран первый элемент"""
    if len(array) < 2:
        return array
    pivot = array[0]
    larger = [i for i in array[1:] if i > pivot]
    lesser = [i for i in array[1:] if i <= pivot]
    return qsort_first(lesser) + [pivot] + qsort_first(larger)


def qsort_random(array):
    """Вариант, когда опорным выбран случайный элемент"""
    if len(array) < 2:
        return array
    else:
        pivot = random.choice(array)
        lesser = []
        larger = []
        equal = []
        for i in array:
            if i < pivot:
                lesser.append(i)
            elif i > pivot:
                larger.append(i)
            else:
                equal.append(i)
        return qsort_random(lesser) + equal + qsort_random(larger)


if __name__ == '__main__':
    array = random.sample(range(2000000), 100)
    print(timeit.timeit(
        "qsort_random(array)", globals=locals()))
    print(timeit.timeit(
        "qsort_first(array)", globals=locals()))
    # a = qsort([1000, 3, 54, 12, 3,  33, 112])
    # print(a)

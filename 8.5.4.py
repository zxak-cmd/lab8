def linear_search(items: list, target) -> int:
    """Линейный поиск: индекс первого вхождения или -1."""
    for i, value in enumerate(items):
        if value == target:
            return i
    return -1
 
 
def binary_search(items: list, target) -> int:
    """Бинарный поиск в отсортированном списке."""
    low, high = 0, len(items) - 1
    while low <= high:
        mid = (low + high) // 2
        if items[mid] == target:
            return mid
        if items[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
 
 
def bubble_sort(items: list) -> list:
    """Сортировка пузырьком (возвращает новый список).""" 
    result = items[:]
    for i in range(len(result)):
        swapped = False
        for j in range(len(result) - 1 - i):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        if not swapped:
            break
    return result
 
 
def filter_items(items: list, predicate) -> list:
    """Фильтрация по условию (функция-предикат)."""
    return [x for x in items if predicate(x)]


print(" 4. Массивы ")

data = [5, 2, 9, 1, 7]

sorted_data = bubble_sort(data)

print(f"Отсортированный массив: {sorted_data} | Исходный массив: {data}")
print(f"Линейный поиск (9): {linear_search(data, 9)}")
print(f"Бинарный поиск (7): {binary_search(sorted_data, 7)}")
print(f"Бинарный поиск (4): {binary_search(sorted_data, 4)}")
print(f"Сортировка пустого списка: {bubble_sort([])}")
print(f"Фильтрация (x > 4): {filter_items(data, lambda x: x > 4)}")

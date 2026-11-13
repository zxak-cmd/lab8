 
def factorial(n: int) -> int:
    """Вычисляет n! рекурсивно."""
    if n < 0:
        raise ValueError("Факториал определён только для n >= 0")
    if n <= 1:  # базовый случай
        return 1
    return n * factorial(n - 1)  # рекурсивный случай
 
 
def factorial_iter(n: int) -> int:
    """Итеративная версия для сравнения."""
    if n < 0:
        raise ValueError("Факториал определён только для n >= 0")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
 
 
def main() -> None:
    """Демонстрация и проверка факториала."""
    for n in (0, 1, 5, 10, 20):
        print(f"{n}! = {factorial(n)}")
    assert all(factorial(n) == factorial_iter(n) for n in range(15))
    print("Рекурсивная и итеративная версии совпадают для n = 0..14")
    try:
        factorial(-3)
    except ValueError as error:
        print("Ошибка:", error)
 
 
if __name__ == "__main__":
    main()
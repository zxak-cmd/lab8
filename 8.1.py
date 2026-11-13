 
def is_prime(n: int) -> bool:
    """Проверяет, является ли число n простым."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
 
 
def main() -> None:
    """Выводит простые числа от 1 до 19 и проверяет краевые случаи."""
    for num in range(1, 20):
        if is_prime(num):
            print(num, end=" ")
    print()  # 2 3 5 7 11 13 17 19
 
    for value in (-7, 0, 1, 2, 97, 100, 7919):
        print(f"is_prime({value}) = {is_prime(value)}")
 
 
if __name__ == "__main__":
    main()
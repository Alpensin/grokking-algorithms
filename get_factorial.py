def factorial(n: int) -> int:
    if n < 2:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    for i in range(1, 15):
        print(f"{i}! =", factorial(i))

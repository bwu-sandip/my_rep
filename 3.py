def fact(n):
    if n == 0:
        return 1
    else:
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        return factorial

num = int(input("Enter a number: "))
print(f"The factorial of {num} is {fact(num)}")

def factorial_test(n):
    if n <= 1:
        return 1
    else:
        return n * factorial_test(n - 1)


x = -1
while x < 0:
    x = int(input('Enter number of factorial'))
    if x < 0:
        print("Please use natural numbers only")

n = factorial_test(x)

print(f"A factorial {x} is {n}")

def recursive_test(n):
    if n <= 9:
        return 1
    else:
        return 1 + recursive_test(n // 10)


print("Decimal exponente of 8 is", recursive_test(8))
print("Decimal exponente of 89 is", recursive_test(89))
print("Decimal exponente of 891 is", recursive_test(891))

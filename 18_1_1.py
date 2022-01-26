def get_sum(number):
    if len(number) == 0:
        return 0
    else:
        return number[0] + get_sum(number[1:])


print(get_sum([2, 3, 4, 6, 12]))


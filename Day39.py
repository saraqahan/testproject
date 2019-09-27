def exponential(power , number):
    if power <1:
        return 1
    else:
        return number * exponential(power -1, number)
print(exponential(3,5))

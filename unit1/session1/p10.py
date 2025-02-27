def split_haycorns(quantity):
    divisors = []
    for i in range(1, quantity + 1):
        if quantity % i == 0:
            divisors.append(i)
    return divisors
quantity = 6
print(split_haycorns(quantity))

quantity = 1
print(split_haycorns(quantity))

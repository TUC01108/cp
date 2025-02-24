def tiggerfy(s):
    leters_to_remove = ['t', 'i', 'g', 'e', 'r']
    t = ''.join([char for char in s if char.lower() not in leters_to_remove])
    return t
s = "suspicerous"
print(tiggerfy(s))

s = "Trigger"
print(tiggerfy(s))

s = "Hunny"
print(tiggerfy(s))

def sum_honey(hunny_jars):
    sum = 0
    for jar in hunny_jars:
        sum += jar
    return sum
    #return sum(hunny_jars)
hunny_jars = [2, 3, 4, 5]
print(sum_honey(hunny_jars))

hunny_jars = []
print(sum_honey(hunny_jars))

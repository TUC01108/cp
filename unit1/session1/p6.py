def doubled(hunny_jars):
    doubled_jars = []
    for jar in hunny_jars:
        jar *= 2
        doubled_jars.append(jar)
    return doubled_jars
hunny_jars = [1, 2, 3]
print(doubled(hunny_jars))

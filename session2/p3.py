def delete_minimum_elements(hunny_jar_sizes):
	hunny_jar_sizes.sort()
	return hunny_jar_sizes
	pass

# Test cases
hunny_jar_sizes = [5, 3, 2, 4, 1]
print(delete_minimum_elements(hunny_jar_sizes))

hunny_jar_sizes = [5, 2, 1, 8, 2]
print(delete_minimum_elements(hunny_jar_sizes))

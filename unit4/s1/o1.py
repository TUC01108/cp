def perfect_pace(n):
    return (n * (n + 1)) / 2 # sum of 1 to n instantly

print(perfect_pace(100))
print(perfect_pace(100000))
print(perfect_pace(100000000))

# loop inside loop = O(n^2)
# three nested loops = O(n^3)
# appending to list = O(1)
# inserting at beginning = O(n)
# quicksort, mergesort, heapsort = O(n log n)
## divide and conquer algorithms = O(n log n)
# bubble sort = O(n^2)
# simple arithmetic operations = O(1)
# Fibonacci implementation = O(2^n)

# O(1)
# O(log n)
# O(n)
# O(n log n)
# O(n^2)
# O(n^3)
# O(2^n)

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print("FIB- ",fibonacci(5))
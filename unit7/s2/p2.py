def find_cabin_index(cabins, preferred_deck):
    def binary_search(left, right):
        if left > right:  # Base case: preferred_deck is not found
            return left  # Return the index where it would be inserted

        mid = (left + right) // 2

        if cabins[mid] == preferred_deck:  # Found the preferred_deck
            return mid
        elif cabins[mid] < preferred_deck:  # Search in the right half
            return binary_search(mid + 1, right)
        else:  # Search in the left half
            return binary_search(left, mid - 1)

    return binary_search(0, len(cabins) - 1)

# Example Usage:

print(find_cabin_index([1, 3, 5, 6], 5))
print(find_cabin_index([1, 3, 5, 6], 2))
print(find_cabin_index([1, 3, 5, 6], 7))

# Example Output:

# 2
# 1
# 4

def count_checked_in_passengers(rooms):
    def binary_search(numbers, value):
        low = 0
        high = len(numbers) - 1
        while low <= high:
            mid = (low + high) // 2
            if numbers[mid] > value:
                high = mid - 1
            elif numbers[mid] < value:
                low = mid + 1
            else:
                numbers.pop(mid)
                count += 1
                print("COUNT",count)

        return None

    # def binary_search(left, right):
    #     if left > right:  # Base case: preferred_deck is not found
    #         return left  # Return the index where it would be inserted

    #     mid = (left + right) // 2

    #     if cabins[mid] < preferred_deck:  # Search in the right half
    #         return binary_search(mid + 1, right)
    #     else:  # Search in the left half
    #         return binary_search(left, mid - 1)

    # return binary_search(0, len(rooms) - 1)
    

# Example Usage:

rooms1 = [0, 0, 0, 1, 1, 1, 1]
rooms2 = [0, 0, 0, 0, 0, 1]
rooms3 = [0, 0, 0, 0, 0, 0]

print(count_checked_in_passengers(rooms1)) 
print(count_checked_in_passengers(rooms2))
print(count_checked_in_passengers(rooms3))

# Example Output:

# 4
# 1
# 0

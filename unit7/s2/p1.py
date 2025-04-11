def find_cruise_length(cruise_lengths, vacation_length):
    left, right = 0, len(cruise_lengths) - 1

    while left <= right:
        mid = (left + right) // 2
        if cruise_lengths[mid] == vacation_length:
            return True  # Found a match
        elif cruise_lengths[mid] < vacation_length:
            left = mid + 1  # Search in the right half
        else:
            right = mid - 1  # Search in the left half

    return False  # No match found


# Example Usage:

print(find_cruise_length([9, 10, 11, 12, 13, 14, 15], 13))

print(find_cruise_length([8, 9, 12, 13, 13, 14, 15], 11))

# Example Output:

# True
# False

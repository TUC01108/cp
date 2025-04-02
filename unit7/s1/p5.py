def power_of_four(n):
    if n == 0:
        return 1
    if n < 0:
        return 1 / power_of_four(-n)
    return 4 * power_of_four(n - 1)

# Example Usage:

print(power_of_four(2))
print(power_of_four(-2))

# Example Output:

# 16
# Example 1 Explanation: 2 to the 4th power (4 * 4) is 16. 
# 16
# Example 2 Explanation: -2 to the 4th power is 1/(4 * 4) is 0.0625.

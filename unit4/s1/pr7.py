def validate_nft_actions(actions):
    sum = 0
    for val in actions:
        if val == "add":
            sum += 1
        if val == "remove":
            sum -= 1
        if sum < 0:
            return False
    return sum == 0

# Example Usage:

actions = ["add", "add", "remove", "remove"]
actions_2 = ["add", "remove", "add", "remove"]
actions_3 = ["add", "remove", "remove", "add"]

print(validate_nft_actions(actions))
print(validate_nft_actions(actions_2))
print(validate_nft_actions(actions_3))

# Example Output:

# True
# True
# False

def final_value_after_operations(operations):
    count = 1  # Initial value of tigger
    for operation in operations:
        if operation == 'bouncy' or operation == 'flouncy':
            count += 1
        elif operation == 'trouncy' or operation == 'pouncy':
            count -= 1
    return count

operations = ["trouncy", "flouncy", "flouncy"]
print(final_value_after_operations(operations))

operations = ["bouncy", "bouncy", "flouncy"]
print(final_value_after_operations(operations))

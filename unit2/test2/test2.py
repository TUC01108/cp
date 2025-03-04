def is_isomorphic(s, t):
     # Step 1: Check if lengths are different
    if len(s) != len(t):
        return False

    # Step 2: Initialize the dictionaries
    s_to_t = {}
    t_to_s = {}

    # Step 3: Iterate through characters of s and t using zip
    for char_s, char_t in zip(s, t):
        # Check if there is an existing mapping for char_s
        if char_s in s_to_t:
            # If the existing mapping does not match char_t, return False
            if s_to_t[char_s] != char_t:
                return False
        else:
            # Create a new mapping from char_s to char_t
            s_to_t[char_s] = char_t

        # Check if there is an existing mapping for char_t
        if char_t in t_to_s:
            # If the existing mapping does not match char_s, return False
            if t_to_s[char_t] != char_s:
                return False
        else:
            # Create a new mapping from char_t to char_s
            t_to_s[char_t] = char_s

    # If all mappings are consistent, return True
    return True

# Example Usage:

# Example 1:
s = "egg"
t = "add"
print(is_isomorphic(s, t))  # Output: True

# Example 2:
s = "foo"
t = "bar"
print(is_isomorphic(s, t))  # Output: False

# Example 3:
s = "paper"
t = "title"
print(is_isomorphic(s, t))  # Output: True
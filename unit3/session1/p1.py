def arrange_guest_arrival_order(arrival_pattern):
    stack = []
    ans = []
    for i in range(len(arrival_pattern)+1):
        if 
        if arrival_pattern[i] == 'I':
            ans.append(str(i + 1))
            if stack:
                ans = ans[0:stack[0]] + ans[stack[0]:][::-1]
                stack = []
            continue
        if arrival_pattern[i] == 'D':
            ans.append(str(i+1))
            if not stack:
                stack.append(i)
    return "".join(ans)
            



  

# Example Usage:

print(arrange_guest_arrival_order("IIIDIDDD"))  
print(arrange_guest_arrival_order("DDD"))  


# You need to create a 0-indexed string guest_order of length n + 1 that satisfies the following conditions:

#     guest_order consists of the digits '1' to '9', where each digit represents the guest's status and is used at most once.
#     If arrival_pattern[i] == 'I', then guest_order[i] < guest_order[i + 1].
#     If arrival_pattern[i] == 'D', then guest_order[i] > guest_order[i + 1].

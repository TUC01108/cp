def welcome():
    s = "Welcome to The Hundred Acre Wood!"
    lst = ['a', 'b', 'c']
    print(s)
    print(len(s))
    print(len(lst))
    # Example 1: Just the stop value 
    x = range(10) # Evaluates to the sequence: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    for n in x:
        print(n, end=' ')
    print()
    # Example 2: Start and stop value
    y = range(1, 11) # Evaluates to the sequence: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    for n in y:
        print(n, end=' ')
    print()
    # Example 3: Start, stop, and step value
    z = range(0, 30, 5) # Evaluates to the sequence: 0, 5, 10, 15, 20, 25
    for n in z: 
        print(n, end=' ')
    print()
    aa = sum([1, 2, 3, 4])
    print(aa)
    bb = min([2, 3, 4, 1, 5])
    print(bb)
    bb = max([2, 3, 4, 1, 5])
    print(bb)
    lst = [1, 2, 3, 4]
    lst.append(5)
    print(lst)
    lst = [4, 2, 1, 3]
    lst.sort()
    print(lst) # Prints [1, 2, 3, 4]
    pass
welcome()
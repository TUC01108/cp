class singly_list:
    def __init__(self, next, value):
        self.value = value
        self.next = next

def intersection(singly_list1, singly_list2):
    head =
    # check if either list is empty then return None.
    if not singly_list1 or singly_list2:
        return None
    # two pointers that iterate through each list when values match then we return that value 
    itr1 = singly_list1.head
    itr2 = singly_list2.head

    while itr1 != itr2:
        itr1 = itr1.next
        itr2 = itr2.next
    return itr1
    

    # else if we make it to end of one or both return None.

singly_list1 = [1,2,3,4,5]
singly_list2 = [9,8,3,4,5]
print(intersection(singly_list1,singly_list2))







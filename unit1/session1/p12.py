def locate_thistles(items):
    thistle_list = []
    for i in range(len(items)):
        if items[i] == "thistle":
            thistle_list.append(i)
    return thistle_list
items = ["thistle", "stick", "carrot", "thistle", "eeyore's tail"]
print(locate_thistles(items))

items = ["book", "bouncy ball", "leaf", "red balloon"]
print(locate_thistles(items))

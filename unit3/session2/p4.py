# At the cultural festival, you are managing a treasure hunt where participants need to visit booths in a specific order. The order in which 
# they should visit the booths is defined by a series of clues. However, some clues lead to dead ends, and participants must backtrack to 
# previous booths to continue their journey.

# You are given a list of clues, where each clue is either a booth number (an integer) to visit or the word "back" indicating that the 
# participant should backtrack to the previous booth.

# Write a function to simulate the participant's journey and return the final sequence of booths visited, in the order they were visited.

def booth_navigation(clues):
    journey = []
    for clue in clues:
        if clue != "back":
            journey.append(clue)
        elif clue == "back" and journey:
            journey.pop()
    return journey
    pass

# Example Usage:

clues = [1, 2, "back", 3, 4]
print(booth_navigation(clues)) 

clues = [5, 3, 2, "back", "back", 7]
print(booth_navigation(clues)) 

clues = [1, "back", 2, "back", "back", 3]
print(booth_navigation(clues)) 

# Example Output:

[1, 3, 4]
[5, 7]
[3]

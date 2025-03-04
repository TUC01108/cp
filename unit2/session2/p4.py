def prioritize_observations(observed_species, priority_species):
    # We have an observed species list and a priority species list.
    # The priority species is distinct and all elements in priority species are also in observed species
    # Write a function that sorts the elements of observed species such that the relative ordering of items 
    # in observed species matches that of priority species. Species that arent in priority species 
    # should be placed at the end of the observed species list in ascending order

    # create one dictionary to store priority species in.. why a dictionary?
    priorityOrderDict = {species: index for index, species in enumerate(priority_species)}
    # print(priorityOrderDict)

    # create two dictionaries? Why dicionaries? No let's use a list
    priority = []
    nonPriority = []

    # for loop to iterate through the species in observed list and check in they are in priority_species list
    # if yes then add them to priority list if not add the to nonPriority
    for species in observed_species:
        if species in priority_species:
            priority.append(species)
        else:
            nonPriority.append(species)
    # sort the priority list based on the priorityOrderDictionary
    priority.sort(key=lambda species: priorityOrderDict[species])
    nonPriority.sort()
    combined = priority + nonPriority
    return combined



    # priorityOrderDictionary = {species: index for index, species in enumerate(priority_species)}

    # # separate the observed_species into priority and non_priority lists
    # priority_list = []
    # non_priority_list = []
    # for species in observed_species:
    #     if species in priorityOrderDictionary:
    #         priority_list.append(species)
    #     else:
    #         non_priority_list.append(species)

    # # sort the priority list based on the priorityOrderDictionary
    # priority_list.sort(key=lambda species: priorityOrderDictionary[species])
    # # sort the non_priority list in ascending order
    # non_priority_list.sort()

    # sorted_observations = priority_list + non_priority_list

    # return sorted_observations
#   pass

# Example Usage:

observed_species1 = ["🐯", "🦁", "🦌", "🦁", "🐯", "🐘", "🐍", "🦑", "🐻", "🐯", "🐼"]
priority_species1 = ["🐯", "🦌", "🐘", "🦁"]  

observed_species2 = ["bluejay", "sparrow", "cardinal", "robin", "crow"]
priority_species2 = ["cardinal", "sparrow", "bluejay"]

print(prioritize_observations(observed_species1, priority_species1))
print(prioritize_observations(observed_species2, priority_species2)) 

# Expected Output:

["🐯", "🐯", "🐯", "🦌", "🐘", "🦁", "🦁", "🐻", "🦑", "🐼", "🐍"]
["cardinal", "sparrow", "bluejay", "crow", "robin"]

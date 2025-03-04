def count_endangered_species(endangered_species, observed_species):

    # understand
    # the function takes in a string of endangered species and a string of observed species
    # we need to go through the string of observed species and count how many times an endangered species appears
    # return that count

    # plan
    keep = set(endangered_species)
    counter = 0
    for species in observed_species1:
        if species in keep:
            counter +=1
    # implement

    return counter

# Example Usage:

endangered_species1 = "aA"
observed_species1 = "aAAbbbb"

endangered_species2 = "z"
observed_species2 = "ZZ"

print(count_endangered_species(endangered_species1, observed_species1)) 
print(count_endangered_species(endangered_species2, observed_species2))  

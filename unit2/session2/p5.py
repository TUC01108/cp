# You are given a 0-indexed integer array species_populations of even length, where each element represents the population of a particular species in a 
# wildlife reserve.

# As long as species_populations is not empty, you must repetitively:

#     Find the species with the minimum population and remove it.
#     Find the species with the maximum population and remove it.
#     Calculate the average population of the two removed species.

# The average of two numbers a and b is (a+b)/2.

# For example, the average of 200 and 300 is (200+300)/2=250.

# Return the number of distinct averages calculated using the above process.

# Note that when there is a tie for a minimum or maximum population, any can be removed.

def distinct_averages(species_populations):
    distinct_averages_set = set()

    # while species_populations is not empty
    while species_populations:
        min_value = min(species_populations)
        max_value = max(species_populations)
        average = (min_value + max_value) / 2
        distinct_averages_set.add(average)
        species_populations.remove(min_value)
        species_populations.remove(max_value)
    return len(distinct_averages_set)
    # find species with min population and remove it
    # find species with the max population and remove it
    # calculate the average of the two removed species using (a+b)/2 and store in a list
# return the number of distinct averages calculated using the above process

# Example Usage:

species_populations1 = [4,1,4,0,3,5]
species_populations2 = [1,100]

print(distinct_averages(species_populations1))
print(distinct_averages(species_populations2)) 

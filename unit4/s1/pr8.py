# Buyers often look for NFTs that are closest in value to their budget. Given a sorted list of NFT values and a budget, you need to find the two NFT values that are closest to 
# the given budget: one that is just below or equal to the budget and one that is just above or equal to the budget. If an exact match exists, it should be included as one of 
# the values.

# Write the find_closest_nft_values() function, which takes a sorted list of NFT values and a budget, and returns the pair of the two closest NFT values.

# Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space 
# complexity.

def find_closest_nft_values(nft_values, budget):
    close_low = nft_values[0]
    close_high = nft_values[len(nft_values)-1]
    for nft in nft_values:
        if nft < budget and close_low < nft:
            close_low = nft
        if nft > budget and close_high > nft:
            close_high = nft

    return [close_low,close_high]

    pass
import bisect

def find_binary(nft_values, budget):
    pos = bisect.bisect_left(nft_values, budget)
    close_low = None
    close_high = None

    if pos > 0:
        close_low = nft_values[pos - 1]

    if pos < len(nft_values):
        close_high = nft_values[pos]

    if close_low is not None and close_high is not None and close_low == budget:
        return [close_low]
    if close_high is not None and close_high == budget:
        return [close_high]
    return [close_low, close_high]
# Example Usage:

nft_values = [3.5, 5.4, 7.2, 9.0, 10.5]
nft_values_2 = [2.0, 4.5, 6.3, 7.8, 12.1]
nft_values_3 = [1.0, 2.5, 4.0, 6.0, 9.0]

print(find_closest_nft_values(nft_values, 8.0))
print(find_closest_nft_values(nft_values_2, 6.5))
print(find_closest_nft_values(nft_values_3, 3.0))
print(find_binary(nft_values, 8.0))
print(find_binary(nft_values_2, 6.5))
print(find_binary(nft_values_3, 3.0))

# Example Output:

# (7.2, 9.0)
# (6.3, 7.8)
# (2.5, 4.0)

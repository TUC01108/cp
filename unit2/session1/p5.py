from collections import Counter
def best_set(votes):
    # Count the occurences of each vote
    vote_counts = Counter(votes.values())
    print(vote_counts)

    # find the vote with the maximum count
    max_vote = max(vote_counts, key=vote_counts.get)

    return max_vote

    pass


votes1 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
    1239: "SZA"
}

votes2 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA"
}

print(best_set(votes1))
print(best_set(votes2))



# print(doubled) # Output: [2, 4, 6, 8, 10]

def reverse_sentence1(string):
    split_string = string.split()
    answerString = ""
    lengthOfString = len(split_string)
    for i in range(lengthOfString - 1, -1, -1):
        answerString += split_string[i] + " "
    return answerString.strip()

def reverse_sentence2(string):
    s = string.split()
    reversedArray = s[::-1] #reverse the list of words
    return ' '.join(reversedArray) # join reversed list into a string

sentence = "tubby little cubby all stuffed with fluff"
print(reverse_sentence2(sentence))

sentence = "Pooh"
print(reverse_sentence2(sentence))

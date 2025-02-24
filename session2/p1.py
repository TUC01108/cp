

# print(doubled) # Output: [2, 4, 6, 8, 10]

# def reverse_sentence(string):
#     split_string = string.split()
#     answerString = ""
#     lengthOfString = len(split_string)
#     for i in range(lengthOfString - 1, -1, -1):
#         answerString += split_string[I] + " "
#     return answerString

from audioop import reverse


def reverse_sentence(string):
    s = string.split()
    reversedArray = ""
    for str in s:
        reversedArray.join(str)
        print(reversedArray)

sentence = "tubby little cubby all stuffed with fluff"
print(reverse_sentence(sentence))

sentence = "Pooh"
print(reverse_sentence(sentence))

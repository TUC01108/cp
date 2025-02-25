def is_acronym(words, s):
    for word in words:
        if word[0] != s[0]:
            return False
        s = s[1:]
        #print(s)
    return True


words = ["christopher", "robin", "milne"]
s = "crm"
print(is_acronym(words, s))

words = ["too", "many", "cooks"]
s = "tmc"
print(is_acronym(words, s))

words = ["four", "many", "cooks"]
s = "fmt"
print(is_acronym(words, s))


#understand
# 


#match

#plan

#implement

#review

#evaluate
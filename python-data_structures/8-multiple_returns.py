#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        t = (0, None)
    else:
        t = (len(sentence), sentence[0])
    return t

sentence = ""
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))
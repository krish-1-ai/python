def match_word(words):
    ctr = 0
    lst = []
    for word in words:
        if len (word) > 1 and word[0] == word[-1]:
            ctr += 1
            lst.append(word)


    print("list of words with the first and last charectar same\n", lst)
    return ctr

count = match_word(['abc', 'cyc', 'xyz', 'aba', '1221' ])
print("number of words having the first and last letter the same:", count)
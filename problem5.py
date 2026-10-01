"""
problem 5
Given a sentence  entered by the user, split into words and count how many times each word appears
"""

def sentence(s: str):
    words = s.split()
    words_set = set()
    frequency = {}

    for word in words:
        if word not in words_set:
            words_set.add(word)
            frequency[word] = 1
        else:
            for aux in frequency:
                if aux == word:
                    frequency[word] += 1

    print(words)
    print(words_set)
    print(frequency)


sentence('welcome to the jungle in the cave')
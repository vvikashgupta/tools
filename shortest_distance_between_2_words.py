from collections import defaultdict
class WordDistance:

    def __init__(self, words):
        self.lst = words
        self.dict = defaultdict(list)
        self.len = len(words)
        print(words)
        for index, word in enumerate(words):
            self.dict[word].append(index)


    def shortest(self, word1, word2):
        if word1 in self.dict:
            lst1 = self.dict[word1]
        if word2 in self.dict:
            lst2 = self.dict[word2]
        print(lst1 , lst2)
        l1_len = len(lst1)
        l2_len = len(lst2)
        i1 = i2 = 0
        distance = self.len
        while i1<l1_len and i2<l2_len:
            distance = min(distance, abs(lst1[i1] - lst2[i2]))
            if lst1[i1] > lst2[i2]:
                i2 += 1
            else:
                i1 += 1
        return distance

class Solution:
    def arrangeWords(self, text: str) -> str:
        from collections import defaultdict
        dict = defaultdict(list)
        len_list = set()
        words = text.split(" ")
        for word in words:
            len_list.add(len(word))
            dict[len(word)].append(word.lower())
        result_set = list(len_list)
        result_set.sort()
        result = []
        for index in result_set:
            result.extend(dict[index])
        result[0] = result[0].capitalize()  
        return " ".join(result)

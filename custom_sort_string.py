from collections import Counter
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        sCounter = Counter(s)
        res = ""
        for char in order:
            if char in sCounter:
                res += char * sCounter[char]
                del sCounter[char]
        for char, count in sCounter.items():
            res += char * count
        return res


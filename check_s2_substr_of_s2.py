class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        c1 = Counter(s1)
        c2 = Counter(s2)
        for k,v in c1.items():
            if k in c2 or v <= c2[k]:
                continue
            else:
                return False
        else:
            return True
        return True

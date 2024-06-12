class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        from collections import Counter, defaultdict
        if len(s) != len(t):
            return False
        seen1 = defaultdict(str)
        seen2 = defaultdict(str)
        '''
        c1 = Counter(s)
        c2 = Counter(t)
        seen = defaultdict()
        s1 = c1.most_common()
        t1 = c2.most_common()
        for i,j in zip(s1,t1):
            if i[1] != j[1]:
                return False
        return True   
        '''
        for i,j in zip(s,t):
            if i not in seen1 and j not in seen2:
                seen1[i] = j
                seen2[j] = i
            elif seen1[i] != j or seen2[j] != i:
                return False
        return True

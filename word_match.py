class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        from collections import defaultdict
        list1 = s.split()
        if len(pattern) != len(list1):
            return False
        seen1 = defaultdict(str)
        seen2 = defaultdict(str)
        for i, j in zip(pattern,list1):
            if i not in seen1 and j not in seen2:
                seen1[i] = j
                seen2[j] = i
            elif seen1[i] != j or seen2[j] != i:
                return False
        return True
        

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        from collections import defaultdict
        d = defaultdict(list)
        for i,val in enumerate(nums):
            d[abs(val)].append(i)  # The index in dict values will always be sorted.
        
        for i,j in d.items():
            if valueDiff == 0:
                if len(j) > 1:
                    start = j[0]
                    for item in j[1:]:
                        if abs(start-item) <= indexDiff:
                            return True
                        else:
                            start = item
                else:
                    continue
            elif valueDiff - abs(i) in d:
                for item in j:
                    for diff in d[valueDiff - abs(i)]:
                        if abs(item - diff) <= valueDiff:
                            return True
            else:
                continue
        return False

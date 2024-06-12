# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 1
        end = n 
        result = -1
        while start <= end:
            pos = start + (end-start)//2
            if isBadVersion(pos):
                end = pos -1 
                result = pos
                if not isBadVersion(pos-1):
                    break
                else:
                    continue
            else:
                start = pos + 1
        return result

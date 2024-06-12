class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        from collections import Counter
        start = end = 0
        c = Counter()
        result = 0
        maxlen = 0
        while end < len(nums):
            c[nums[end]] += 1
            
            if c[nums[end]] > k:
                while c[nums[end]] <= k:
                    c[nums[start]] -= 1
                    start += 1
            else:
                maxlen = max(maxlen, end - start + 1)
                
            end += 1
        return maxlen

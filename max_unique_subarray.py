class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        from collections import defaultdict, deque, Counter
        start = end = 0
        result = deque()
        maxsum = curr = 0
        while end < len(nums):
            if nums[end]  in result:
                while result:
                    #A duplicate is found
                    popped = result.popleft()
                    curr -= popped
                    if popped == nums[end]:
                        break
            result.append(nums[end])
            curr += nums[end]
            end += 1
            maxsum = max(maxsum, curr)
            
        return maxsum

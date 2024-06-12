class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        print(f'{nums},{k}')
        start = end = maxlen = 0
        curr_sum = 0
        psum = [nums[0]]
        from collections import defaultdict
        sumdict = defaultdict()
        sumdict[nums[0]] = 0
        
        for index,num in enumerate(nums[1:]):
            
            psum.append(num + psum[-1])
            print(f'{index},{num},{psum}')
            if psum[-1] == k:
                maxlen = max(maxlen, index + 2)
                print(f'set maxlen to {maxlen}')
            if psum[-1] - k in sumdict:
                maxlen = max(maxlen,index - sumdict[psum[-1] - k] + 1)
                print(f'set maxlen from dict to {maxlen}')
            if psum[-1] not in sumdict:
                sumdict[psum[-1]] = index

        
        return maxlen

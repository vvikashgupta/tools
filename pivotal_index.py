class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        psum = [0]
        for num in nums:
            psum.append(psum[-1]+num)
        #print(psum)
        for i in range(1,len(psum)):
            lsum = psum[i-1]
            rsum = psum[-1] - psum[i]
            #print(f'{lsum}.{rsum}')
            if lsum == rsum:
                return i-1
        return -1

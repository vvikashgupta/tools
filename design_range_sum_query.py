class NumArray:

    def __init__(self, nums: List[int]):
        self.psum = [nums[0]]
        self.nums = nums
        for num in nums[1:]:
            self.psum.append(self.psum[-1] + num)
        

    def sumRange(self, left: int, right: int) -> int:
        return self.psum[right] - self.psum[left] + self.nums[left]
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = fast = 0
        while fast < len(nums):
            if nums[slow] == 0:
                nums.append(nums.pop(slow))
            else:
                slow += 1
            fast += 1

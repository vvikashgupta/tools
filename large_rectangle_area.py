#!/usr/local/bin/python

class Solution:
    def largestRectangleArea(self, heights):
        print("largestRectangleArea")
        max_area = 0
        def calc_area(nums):
            print(f'calc_area {nums}')
            nonlocal max_area
            if not nums:
                return
            area = min(nums) * len(nums)
            max_area = max(area, max_area)
            print(f'max_area is {max_area}')
        
        def divide_nums(nums):
            print(f'divide_nums {nums}')
            if not nums :
                return 0
            calc_area(nums)
            if len(nums) == 1:
                return
            min_num = min(nums)
            min_index = nums.index(min_num)
            print(f'{min_num}, {min_index}')
            if min_index == 0:
                min_index = 1
            if min_index == len(nums):
                min_index -= 1
            divide_nums(nums[0:min_index])
            divide_nums(nums[min_index:])
            
        divide_nums(heights)
        return max_area

def main():
    s = Solution()
    lst = [2,1,5,6,2,3]
    print(s.largestRectangleArea(lst))
    #print(s.largestRectangleArea([1]))

if __name__ == '__main__':
    main()

#!/usr/local/bin/python



def partition(nums, lo, hi):
    pivot = nums[hi]
    i = lo
    for index in range(lo, hi):
        if nums[index] < pivot:
            nums[i],nums[index] = nums[index],nums[i]
            i += 1
    nums[i],nums[hi] = nums[hi],nums[i]
    print(i)
    return i


def qsort(nums, lo, hi):
    if lo < hi:
        p = partition(nums, lo, hi)
        qsort(nums, lo, p-1)
        qsort(nums, p+1, hi)

def quicksort(nums):
    print( nums)
    if not nums: return nums

    return qsort(nums, 0, len(nums)-1)

def main():
    nums = [1,5,3,2,8,7,6,4]
    print(quicksort(nums))
    print( nums)

if __name__ == '__main__':
    main()

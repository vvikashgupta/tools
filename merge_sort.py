#!/usr/local/bin/python

class Sort:
    def __init__(self):
        print('Merge Sort')

    @staticmethod
    def merge_sort(nums):
        if len(nums) <= 1:
            return nums

        pivot = len(nums) // 2
        left_list = Sort.merge_sort(nums[0:pivot])
        right_list = Sort.merge_sort(nums[pivot:])
        return Sort.merge(left_list, right_list)

    @staticmethod
    def merge(left_list, right_list):
        left_index = right_index = 0
        result = []
        while left_index < len(left_list) and right_index < len(right_list):
            if left_list[left_index] < right_list[right_index]:
                result.append(left_list[left_index])
                left_index += 1
            else:
                result.append(right_list[right_index])
                right_index += 1
        #Now there is a possibility that some of the list is not exhausted.
        result.extend(left_list[left_index:])
        result.extend(right_list[right_index:])
        return result

def main():
    print(Sort.merge_sort([1,5,3,2,2,7,4,1,8,7,6,4]))
    

if __name__ == '__main__':
    main()

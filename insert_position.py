def searchInsert(nums, target):
    start = 0
    end = len(nums) -1
    result = -1
    print(nums)
    print(start, end)
    while start <= end :
        pos = (start + end)//2
        print(pos, start , end)
        if target == nums[pos]:
            result = pos
            break
        elif target < nums[pos]:
            end = pos + 1
        else:
            start = pos + 1
    else:
        if target > nums[pos]:
            result = pos -1
        else:
            result = pos
    return result

def main():
	print(searchInsert([1,3,5,6],5))
	print(searchInsert([1,3],2))




if __name__=='__main__':
	main()

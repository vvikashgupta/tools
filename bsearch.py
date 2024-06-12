#import sys,os


def search(nums, target):
    start = 0
    end = len(nums) - 1 
    result = -1
    print(nums)
    print(start,end)
    while start <= end:
        pos = (start+end)//2
        num = nums[pos]
        print(f'{pos},{num}')
        if target == num:
            result = pos
            break
        elif target < num:
            end = pos - 1
        else:
            start = pos + 1
    return result


def main():
    search([-1,0,3,5,9,12],9)

if __name__ == '__main__':
    main()

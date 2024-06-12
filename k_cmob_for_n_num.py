#!/usr/local/bin/python



class Solution:
    def combine(self, n, k):
        result = []
        def helper(nums, next=1):
            print(f'Helper called with {nums}') 
            if len(nums) >= k:
                print(f'nums is equal to k length {nums} , {k}')
                #if nums not in result:
                #    print(f'result = {result}')
                result.append(nums[:])
                print(f'result = {result}')
                print('Returning')
                return
            for i in range(next,n+1):
                nums.append(i)
                print(f'Appending i to nums {i},{nums}')
                helper(nums, i+1)
                nums.pop()

        
        helper([])
        return result

    def combine_new(self, n , k):
        import itertools as it
        lst = [ x for x in range(1,n+1)]
        result = list(it.combinations(lst, k))
        return result

def main():
    s = Solution()
    print(s.combine(4,2))
    print(s.combine_new(4,2))

if __name__ == '__main__':
    main()

class Solution:
    def climbStairs(self, n: int) -> int:
        from collections import defaultdict
        dict = defaultdict()
        result = 0
        step_size = [1, 2]
        
        def helper(num):
            nonlocal result, dict
            if num > n:
                return 0
            elif num == n: # Reached the final step
                result += 1
                return 1
            else:
                pass
            
            if num in dict: # This step is already visited and store.
                result += dict[num] # Since we have no. of ways directly add them to result.
                return dict[num]
            
            n1 = helper(num+1)
            n2 = helper(num+2)
            dict[num] = n1 + n2
            return dict[num]
            
        helper(0)
        return result

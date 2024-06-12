class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        from collections import deque
        vowels = ['a','e','i','o','u']
        fast = 0
        maxv = 0
        result = deque()
        
        def count_vowels(st):
            maxcount = sum([ 1 for x in st if x in vowels])
            #print(maxcount)
            return maxcount
        
        print(len(s))
        print(count_vowels(s))
        '''
        while fast+k <= len(s):
            count = count_vowels(s[fast:fast+k])
            maxv = max(count, maxv)
            fast += 1
        print(maxv)
        return maxv
        '''
        for i in range(k):
            result.append(s[i])
        maxvowels = 0
        maxv = count_vowels(result)
        #print(maxv)
        maxvowels = max(maxvowels, maxv)
        while fast+k < len(s) :
            #print(f'{fast+k},{len(s)} {maxv}, {maxvowels}')
            result.append(s[fast+k])
            d = result.popleft()
            if d in vowels:
                #print('reducing maxv by 1')
                maxv -= 1
            if result[-1] in vowels:
                #print('increasing maxv by 1')
                maxv += 1
            maxvowels = max(maxvowels, maxv)
            fast += 1
        return maxvowels
            
            
        

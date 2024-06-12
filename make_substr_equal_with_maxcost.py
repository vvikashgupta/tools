class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        #In this problem, let us first calculate a diff-arrag
        # Now do a prefix-sum of this array.
        # Now find the max-sum equal to maxCost
        diff = [abs(ord(a) - ord(b)) for a,b in zip(s,t)]
        print(diff)
        #psum = [diff[0]]
        #for num in diff[1:]:
        #    psum.append(num + psum[-1])
        #print(psum)
        
        curr = 0
        slow = 0
        fast = 0
        maxchange = 0
        while fast < len(diff):
            curr += diff[fast]
            if curr == maxCost:
                maxchange = max(maxchange, fast - slow + 1)
            elif curr > maxCost:
                maxchange = max(maxchange, fast - slow)
            else:
                pass
            
            while curr > maxCost:
                curr -= diff[slow]
                slow += 1
            fast += 1
        return maxchange
        

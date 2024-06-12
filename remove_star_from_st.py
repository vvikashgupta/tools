class Solution:
'''
Input: s = "leet**cod*e"
Output: "lecoe"
'''
    def removeStars(self, s: str) -> str:
        result = []
        for char in s:
            if char != '*':
                result.append(char)
            else:
                if result:
                    result.pop()
        return "".join(result)

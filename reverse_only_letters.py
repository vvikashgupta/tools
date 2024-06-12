class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        result = [x for x in s]
        start = 0
        end = len(result) - 1
        while start < end:
            while not result[start].isalpha():
                start += 1
                if start >= len(result)-1:
                    break
            while not result[end].isalpha():
                end -= 1
                if end < 0:
                    break
            
            result[start],result[end] = result[end],result[start]
            start += 1
            end -= 1
        return "".join(result)

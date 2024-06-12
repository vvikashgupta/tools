class Solution:
    def reverseWords(self, s: str) -> str:
        def reverse_word(word):
            print(word)
            slen = len(word) - 1
            index = 0
            result = [0]*(slen + 1)
            while index <= len(word)//2:
                result[index], result[slen] = word[slen],word[index]
                index += 1
                slen -= 1
            print(result)
            return "".join(result)
            #return word.reverse()
        
        result = []
        lst = s.split()
        for word in lst:
            print(word)
            rword = reverse_word(word)
            print(rword)
            result.append(rword)
            #result.append(reverse_word(word))
        return ' '.join(result)

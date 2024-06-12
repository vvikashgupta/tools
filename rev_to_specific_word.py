class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:

        def rev_str(chars):
            print(chars)
            start = 0
            end = len(chars) -1 
            while start < len(chars)//2:
                chars[start],chars[end] = chars[end],chars[start]
                start += 1
                end -= 1
            print(chars)
            return chars

        if ch not in word:
            return word
        lst = [c for c in word]
        index = word.index(ch)
        #print(f'{ch},{lst}')
        #print(lst[0:index+1].reverse())
        first_part = rev_str(lst[0:index+1])
        last_part = lst[index+1:]
        print(first_part,last_part)
        first_part.extend(last_part)
        return "".join(first_part)
        print(first_part)
        #return "".join(first_part.extend(lst[index+1:]))
        #print(lst)
        #return "".join(lst)    

#!/usr/local/bin/python

class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        print(f'str is {s}')
        if not s or len(s) ==1:
            print('return from here')
            return
        self.reverseString(s[1:(len(s)-1)])
        s[0] , s[-1] = s[-1],s[0]
        print(f'new s is not {s}')

def main():
    s = ["k","h","e","l","l","o","p"]
    Solu = Solution()
    print(s)
    Solu.reverseString(s)
    print(s)

if __name__ == "__main__":
    main()

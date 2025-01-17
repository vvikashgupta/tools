#!/usr/local/bin/python
Google soltuion for NQueen question
'''
class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        def is_not_under_attack(row, col):
            return not (rows[col] or hills[row - col] or dales[row + col])
        
        def place_queen(row, col):
            rows[col] = 1
            hills[row - col] = 1  # "hill" diagonals
            dales[row + col] = 1  # "dale" diagonals
        
        def remove_queen(row, col):
            rows[col] = 0
            hills[row - col] = 0  # "hill" diagonals
            dales[row + col] = 0  # "dale" diagonals
        
        def backtrack(row = 0, count = 0):
            for col in range(n):
                if is_not_under_attack(row, col):
                    place_queen(row, col)
                    if row + 1 == n:
                        count += 1
                    else:
                        count = backtrack(row + 1, count)
                    remove_queen(row, col)
            return count
        
        rows = [0] * n
        hills = [0] * (2 * n - 1)  # "hill" diagonals
        dales = [0] * (2 * n - 1)  # "dale" diagonals
        return backtrack()
'''
class Solution:
    def __init__(self):
        print("Solution:")

    @staticmethod
    def is_under_attack(row, col):
    return (rows[cols] or hills[row-col] or dales[row+col]

    @staticmethod
    def place_queen(row, col):
        rows[col] = 1
        hills[row-col] = 1
        dales[row+col] = 1
    @staticmethod
    def remove_queen(row, col):
        rows[col] = 0
        hills[row-col] = 0
        dales[row+col] = 0
        
    @staticmethod
    def backtrace(row = 0, count = 0 ):
        for col in range(n):
            if not is_under_attack(row,col):
                place_queen(row, col)
                if row + 1 == count:
                    count += 1
                else:
                    backtrace(row+1, count)
                remove_queen(row, col)


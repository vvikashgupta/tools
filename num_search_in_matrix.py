#!/usr/local/bin/python

import cProfile


def find_number_in_array(row , target):
    print(row)
    left = 0 
    right = len(row)
    found = False
    while left < right:
        mid = (left + right)//2
        if target == row[mid]:
            return True
        elif target < row[mid]:
            right = mid
        else:
            left = mid + 1

def searchMatrix(matrix, target):
    transpose = list(zip(*matrix))
    print(f' {matrix}, {transpose}')
    rows = len(matrix)
    cols = len(matrix[0])
    for index in range(min(rows,cols)):
       search = find_number_in_array(matrix[index], target)
       search_transpose = find_number_in_array(transpose[index], target)  
       if search or search_transpose:
           return True
    return False

def simple(matrix, target):
    for row in matrix:
        if target in row:
            return True
    return False

#def numpy_simple(matrix, target):


def main():
    matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
    print(searchMatrix(matrix,5))
    print(simple(matrix,5))


if __name__ == '__main__':
    main()

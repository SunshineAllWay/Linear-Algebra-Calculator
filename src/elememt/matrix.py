# -*- coding: utf-8 -*-
"""
@author: Sunshine Wang

This module contains some useful functions for dealing with matrix

Overview:
- class Matrix
    Overview about the methods:
         __str__() : returns a string representation
         operator * : implements the matrix vector multiplication
         implements the matrix-scalar multiplication.
         changeComponent(x,y,value) : changes the specified component.
         component(x,y) : returns the specified component.
         width() : returns the width of the matrix
         height() : returns the height of the matrix
         operator + : implements the matrix-addition.
         operator - _ implements the matrix-subtraction

- function squareZeroMatrix(N)
- function randomMatrix(W,H,a,b)
"""


class Matrix(object):

    # constructor
    def __init__(self, matrix, row, col):
        self.__matrix = matrix
        self.__col = col
        self.__row = row

    # return a string representation of the matrix
    def __str__(self):
        ans = ""
        for i in range(self.__row):
            ans += "|"
            for j in range(self.__col):
                if j < self.__col - 1:
                    ans += str(self.__matrix[i][j]) + ","
                else:
                    ans += str(self.__matrix[i][j]) + "|\n"
        return ans

    # return the column number of matrix
    def col(self):
        return self.__col

    # return the row number of matrix
    def row(self):
        return self.__row


def main():
    A = Matrix([[1, 2, 3], [2, 4, 5]], 2, 3)
    print(A)
    print(A.row())
    print(A.col())


if __name__ == "__main__":
    main()




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
         row() : returns the count of rows of the matrix
         col() : returns the count of columns of the matrix
         operator + : implements the matrix-addition.
         operator - _ implements the matrix-subtraction
         transpose : transpose the matrix

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

    # multiple with a matrix
    def multiple_matrix(self, A):
        if self.col() != A.row():
            return None
        else:
            matrix = []
            for i in range(self.row()):
                singlerow = []
                for j in range(A.col()):
                    acc = 0
                    for k in range(self.col()):
                        acc += self.__matrix[i][k] * A.element(k, j);
                    singlerow.append(acc)
                matrix.append(singlerow)
            C = Matrix(matrix, self.row(), A.col())
            return C

    # multiple with a scalar
    def multiple_scalar(self, c):
        for i in range(self.row()):
            for j in range(self.col()):
                self.__matrix[i][j] *= c
        return self

    # change the element at (x, y) to value
    def changeComponent(self, x, y, value):
        self.__matrix[x][y] = value

    # get component at the specific pix
    def component(self, x, y):
        return self.__matrix[x][y];

    # transpose the matrix
    def transpose(self):
        matrix = []
        for i in range(self.__col):
            singlerow = []
            for j in range(self.__row):
                singlerow.append(self.__matrix[j][i])
            matrix.append(singlerow)
        at = Matrix(matrix, self.__col, self.__row)
        return at

    # add
    def __add__(self, A):
        if self.row() != A.row() or self.col() != A.col():
            raise Exception("two matrix must be in the same size")
        component = []
        for i in range(self.row()):
            singlerow = []
            for j in range(A.col()):
                singlerow.append(self.component(i, j) + A.component(i, j))
            component.append(singlerow)
        B = Matrix(component, self.row(), self.col())
        return B

    # subtract
    def __sub__(self, A):
        if self.row() != A.row() or self.col() != A.col():
            raise Exception("two matrix must be in the same size")
        return self + A.multiple_scalar(-1.0)


def main():
    A = Matrix([[1, 2, 3], [2, 4, 5]], 2, 3)
    B = Matrix([[1, 0], [0, 1], [0, 0]], 3, 2)
    C = Matrix([[1, 1, 1], [1, 1, 1]], 2, 3)
    print(A)
    print(A.row())
    print(A.col())
    print(B)
    print(B.row())
    print(B.col())
    D = A.multiple_matrix(B)
    print(A.multiple_scalar(-1.0))
    print(A - C)


if __name__ == "__main__":
    main()




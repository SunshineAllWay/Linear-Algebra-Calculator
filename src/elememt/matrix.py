# -*- coding: utf-8 -*-
"""
@author: Sunshine Wang

This module contains some useful functions for dealing with matrix

Overview:
- class Matrix
- function squareZeroMatrix(N)
- function randomMatrix(W,H,a,b)
"""


class Matrix(object):
    """
    class: Matrix
    This class represents a arbitrary matrix.

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
    """

    def __init__(self, matrix, w, h):
        """
            simple constructor for initialzes
            the matrix with components.
        """
        self.__matrix = matrix
        self.__width = w
        self.__height = h
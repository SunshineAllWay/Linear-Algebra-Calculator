# -*- coding: utf-8 -*-
"""
@author: Sunshine Wang

This module contains some useful functions for dealing with vector

Overview:
- class Vector
- function zeroVector(dimension)
- function unitBasisVector(dimension,pos)
- function axpy(scalar,vector1,vector2)
- function randomVector(N,a,b)
"""

import math
import random

class Vector(object):

    # contructor
    def __init__(self, components):
        self.__components = components


    # set components in the vector
    def set(self, components):
        self.__components = components


    # return a string representation of the vector
    def __str__(self):
        ans = "("
        length = len(self.__components)
        for i in range(length):
            if i != range(length):
                ans += str(self.__components[i]) + ","
            else:
                ans += str(self.__components[i]) + ")"
        if len(ans) == 1:
            ans += ")"              # empty vector
        return ans


    # return the dimension of vector
    def dimension(self):
        return len(self.__components)


    # return the i-th component
    def component(self, i):
        if i < dimension(self):
            return self.__components[i]
        else:
            return None

    # add
    def add(self, v):
        if dimension(v) != dimension(self):
            return None

        length = dimension(self)
        for i in range(length):
            self.__components[i] += v.component(i)



def main():
    Vector v1([1,2,3])
    Vector v2([2,3,4])
    print (v1)

if __name__ == "__main__":
    main()



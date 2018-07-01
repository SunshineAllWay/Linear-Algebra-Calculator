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

import  math
import random

class Vector(object):

    # contructor
    def __init__(self, components):
        self.__components = components

    # set components in the vector
    def set(self, components):
        self.__components = components

    # returns a string representation of the vector
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



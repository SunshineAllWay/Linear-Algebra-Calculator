# -*- coding: utf-8 -*-
"""
@author: Sunshine Wang

This module contains some useful functions for dealing with vector

    constructor(components : list) : init the vector
    set(components : list) : changes the vector components.
    __str__() : toString method
    dimension() : gets the dimension of the vector (number of components)
    component(i : int): gets the i-th component (start by 0)
    euclidLength() : returns the eulidean length of the vector.

    operator + : vector addition
    operator - : vector subtraction
    operator * : scalar multiplication and dot product
    inner product: inner product of
    copy() : copies this vector and returns it.

    changeComponent(pos,value) : changes the specified component.
"""


class Vector(object):
    # constructor
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
            if i != length - 1:
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
        if i < self.dimension():
            return self.__components[i]
        else:
            return None

    # addition
    def __add__(self, other):
        result = []
        dim = self.dimension();
        if other.dimension() == dim:
            for i in range(dim):
                result.append(self.__components[i] + other.component(i))
        else:
            raise Exception("two vectors must be in the same dimension");
        return Vector(result)

    # subtraction
    def __sub__(self, other):
        result = []
        dim = self.dimension()
        if other.dimension() == dim:
            for i in range(dim):
                result.append(self.__components[i] - other.component(i))
        else:
            raise Exception("two vectors must be in the same dimension");
        return Vector(result)

    # scalar product or inner product
    def __mul__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return self.scalar_product(other)
        if isinstance(other, Vector) and self.dimension() == other.dimension():
            return self.inner_product(other)
        return None

    # scalar product
    def scalar_product(self, other):
        result = []
        dim = self.dimension()
        for i in range(dim):
            result.append(self.__components[i] * other)
        return Vector(result)

    # inner product
    def inner_product(self, other):
        result = 0
        dim = self.dimension();
        if other.dimension() == dim:
            for i in range(dim):
                result += self.__components[i] * other.component(i)
        else:
            raise Exception("two vectors must be in the same dimension");
        return result


def main():
    v1 = Vector([1, 2, 3])
    v2 = Vector([2, 3, 4])
    print(v1 + v2)
    print(v1 - v2)
    print(v1 * 3)
    print (v1 * v2)
    print(v1.inner_product(v2))


if __name__ == "__main__":
    main()



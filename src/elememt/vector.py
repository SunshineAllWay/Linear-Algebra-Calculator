# -*- coding: utf-8 -*-
"""
@author: Sunshine Wang

This module contains some useful functions for dealing with vector

    constructor(components : list) : init the vector
    set(components : list) : changes the vector components.
    __str__() : toString method
    dimension() : gets the dimension of the vector (number of components)
    component(i : int): gets the i-th component (start by 0)
    change_component(pos,value) : changes the specified component.
    euclidLength() : returns the eulidean length of the vector.

    operator + : vector addition
    operator - : vector subtraction
    operator * : scalar multiplication and dot product
    inner product: inner product of two vector
    scalar product: scalar product of vector and a number

    pure_vector: return vector containing the same number
    zero_vector: return vector containing 0
    unit_base_vector: return the unit base vector
    random_vector: return the vector containing the random numbers between 0 to 1
"""
import math
import random


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

    # changes the specified component
    def change_component(self, pos, value):
        if self.dimension() > pos:
            self.__components[pos] = value
            return self
        else:
            raise Exception("index exceed the limit")

    # return euclid length of vector
    def euclid_length(self):
        result = 0
        dim = self.dimension()
        for i in range(dim):
            result += self.__components[i] * self.__components[i]
        return math.sqrt(result)

    # addition
    def __add__(self, other):
        result = []
        dim = self.dimension()
        if other.dimension() == dim:
            for i in range(dim):
                result.append(self.__components[i] + other.component(i))
        else:
            raise Exception("two vectors must be in the same dimension")
        return Vector(result)

    # subtraction
    def __sub__(self, other):
        result = []
        dim = self.dimension()
        if other.dimension() == dim:
            for i in range(dim):
                result.append(self.__components[i] - other.component(i))
        else:
            raise Exception("two vectors must be in the same dimension")
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
        dim = self.dimension()
        if other.dimension() == dim:
            for i in range(dim):
                result += self.__components[i] * other.component(i)
        else:
            raise Exception("two vectors must be in the same dimension")
        return result


# return vector containing the same number
def pure_vector(dim, a):
    result = []
    for i in range(dim):
        result.append(a)
    return Vector(result)


# return vector containing 0
def zero_vector(dim):
    return pure_vector(dim, 0)


# return the unit base vector
def unit_base_vector(dim, pos):
    v = zero_vector(dim)
    v.change_component(pos, 1)
    return v


# return the vector containing the random numbers between 0 to 1
def random_vector(dim):
    result = []
    for i in range(dim):
        result.append(random.random())
    return Vector(result)


def main():
    v1 = Vector([1, 2, 3])
    v2 = Vector([2, 3, 4])
    print(v1 + v2)
    print(v1 - v2)
    print(v1 * 3.0)
    print(v1 * v2)
    print(v1.inner_product(v2))
    print(v1.change_component(2, 0))
    print(v1.euclid_length())

    u1 = zero_vector(3)
    u3 = unit_base_vector(3, 0)
    u4 = random_vector(3)
    u5 = pure_vector(3, 6)
    print(u1)
    print(u3)
    print(u4)
    print(u5)


if __name__ == "__main__":
    main()



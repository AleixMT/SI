#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys


class Magnitude:

    SI_magnitudes = (("m", "meters", "length"), ("g", "grams", "mass"), ("s", "seconds", "time"), ("K", "Kelvin", "temperature"), ("A", "Ampere", "electric current"), ("mol", "mol", "molar concentration"), ("cd", "Candela", "luminous intensity"))

    SI_submultiples = (("Y", "yotta"), ("Z", "zetta"), ("E", "exa"), ("P", "peta"), ("T", "tera"), ("G", "giga"), ("M", "mega"), ("k", "kilo"), ("h", "hecto"), ("da", "deca"), ("", ""), ("d", "deci"), ("c", "centi"), ("m", "mili"), ("µ", "micro"), ("n", "nano"), ("p", "pico"), ("f", "femto"), ("a", "atto"), ("z", "zepto"), ("y", "yocto"))

    SI_submultiple_values = (1000., 1000., 1000., 1000., 1000., 1000., 1000., 10., 10., 10., 10., 10., 10., 1000., 1000., 1000., 1000., 1000., 1000., 1000.)

    def __init__(self):
        pass

    # compares the submultiple of the given parameter to the submultiple of the self object.
    # Returns 1 if self.submultiple is bigger than the submultiple given by parameter
    # Returns 0 if self.submultiple is equal than the submultiple given by parameter
    # Returns -1 if self.submultiple is smaller than the submultiple given by parameter
    def compareTo(self, submultiple):

        if self.submultiple_position(submultiple) > self.submultiple_position(self.submultiple):
            return 1
        elif self.submultiple_position(submultiple) == self.submultiple_position(self.submultiple):
            return 0
        else:
            return -1

    # Returns the position to index in the list of tuples SI_submultiple_values as follows:
    # yotta = 0, zetta = 1, ... , "" = 10, ... , yocto = 20
    def submultiple_position(self, submultiple):
        for i in range(len(self.SI_submultiples)):
            if submultiple == self.SI_submultiples[i][0] or submultiple == self.SI_submultiples[i][1]:
                return i

    # Converts the self magnitude to the submultiple given by parameter.
    # To do it it distinguish if it is doing an incrementative or decrementative conversion
    def convert(self, submultiple):
        if self.compareTo(submultiple) == 1:
            for i in range(self.submultiple_position(self.submultiple), self.submultiple_position(submultiple)):
                self.value = float(self.value) * self.SI_submultiple_values[i]
        elif self.compareTo(submultiple) == -1:
            for i in range(self.submultiple_position(self.submultiple) - 1, self.submultiple_position(submultiple) - 1, -1):
                self.value = float(self.value) / self.SI_submultiple_values[i]
        self.submultiple = submultiple
        return self.value

    def toString(self):
        msg = "{:e}".format(self.value) + " " + self.submultiple + self.magnitude
        return msg

    def checkSubmultiple(self, unit):
        for i in self.SI_magnitudes:
            if unit.endswith(i[0]):
                unit = unit[:-len(i[0])]
            for j in self.SI_submultiples:
                    if j[0].__eq__(unit):
                        return unit
                    if j[1].__eq__(unit):
                        return unit
            if unit.endswith(i[1]):
                unit = unit[:-len(i[1])]
                for j in self.SI_submultiples:
                    if j[0].__eq__(unit):
                        return unit
                    if j[1].__eq__(unit):
                        return unit
        print("ERROR: not recognized submultiple")
        exit(1)

    def trimInput(self, value, originunit, destinyunit):
        try:
            value = float(value)
        except ValueError:
            print("Error 1: Incorrect value from 1st argument must be a number")
            exit(1)
        originsubmultiple, originmagnitude = "", ""
        try:
            originunit = str(originunit)
            originsubmultiple = self.checkSubmultiple(originunit)
            originmagnitude = originunit.lstrip(originsubmultiple)
            # Amb la info del submultiple de la unitat origen, trobar la magnitud de la unitat
        except ValueError:
            print("Error 2: Incorrect value from 2nd argument must be string type")
            exit(1)

        destinysubmultiple, destinymagnitude = "", ""
        try:
            destinyunit = str(destinyunit)
            destinysubmultiple = self.checkSubmultiple(destinyunit)
            destinymagnitude = destinyunit.lstrip(destinysubmultiple)

        except ValueError:
             print("Error 3: Incorrect value from 3rd argument must be string type")
             exit(1)

        self.value = value
        self.submultiple = originsubmultiple
        self.magnitude = originmagnitude

        return destinysubmultiple

# Process stdin
if not sys.stdin.isatty():
    # trim input and create a new Magnitude Object with the given data, save the submultiple destiny
    # Then, call convert function passing the submultiple destiny and print the result of it
    y = sys.stdin.readlines()[0].rstrip("\n").lstrip("\n")
    y = y.split()
    if len(y) != 3:
        for i in y:
            print(i)
        print("ERROR: SI needs three arguments")
        exit(2)
    magn = Magnitude()
    destinysubmultiple = magn.trimInput(y[0], y[1], y[2])
    magn.convert(destinysubmultiple)
    print(magn.toString())
    exit(0)

# Process arguments
if len(sys.argv) != 4:
    print("ERROR: SI needs three arguments")
    exit(2)

magn = Magnitude()
destinysubmultiple = magn.trimInput(sys.argv[1], sys.argv[2], sys.argv[3])
magn.convert(destinysubmultiple)
print(magn.toString())

exit(0)

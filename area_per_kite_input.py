#!/usr/bin/env python3
# Created By: Angel
# Date: March 03,2025
# This program asks the user for the length P,
# length Q for the perimeter and the side A and
# side B for the area of a kite. It the calculates
#  the area and perimeter of a kite.


import math


def main():

    # get the length P and Q from the user
    P = float(input("Enter the length of diagonal" " P (mm): "))
    Q = float(input("Enter the length of diagonal " "Q (mm): "))

    # get the side A and B from the user
    sideA = float(
        input("Enter the length side A " "(first pair of equal sides) (mm): ")
    )
    sideB = float(
        input("Enter the length side B" " (second pair of equal signs) (mm): ")
    )

    # calculates the perimeter and area
    area = (P * Q) / 2
    perimeter = 2 * (sideA + sideB)

    # display the perimeter and area
    print("")
    print("Area = {} cm^2", format(area))
    print("perimeter = {}cm".format(perimeter))


if __name__ == "__main__":
    main()

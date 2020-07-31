import numpy as nu
from numpy import *
import math

option=input("Scalar product(Dot product) or Vector product(Cross product): ")

def ScalarProduct():
    print("Vector A")
    Ai = float(input("Enter Ai:"))
    Aj = float(input("Enter Aj:"))
    Ak = float(input("Enter Ak:"))
    a=[Ai, Aj, Ak]

    print("\nVector B")
    Bi = float(input("Enter Bi:"))
    Bj = float(input("Enter Bj:"))
    Bk = float(input("Enter Bk:"))
    b=[Bi, Bj, Bk]

    MagA = sqrt((Ai ** 2) + (Aj ** 2) + (Ak ** 2))
    MagA = round(MagA, 2)
    MagB = sqrt((Bi ** 2) + (Bj ** 2) + (Bk ** 2))
    MagB = round(MagB, 2)
   # ans = (Ai * Bi) + (Aj * Bj) + (Ak * Bk)
    ans = nu.dot(a,b)
    ans = round(ans, 2)
    s = ans / (MagA * MagB)
    angle = nu.arccos(s)
    angle = angle * (180 / pi)
    x = "The scalar product of vectors A and B is: " + str(ans) + "\nThe magnitude of A: " + str(MagA) + \
        "\nThe magnitude of B: " + str(MagB) + "\nThe angle: " + str(round(angle, 2)) + " degrees" + \
        "\nAnd in radians: " + str(round((angle * pi / 180), 2)) + " radians"

    return x


def VectorProduct():
    print("Vector A")
    Ai = float(input("Enter Ai:"))
    Aj = float(input("Enter Aj:"))
    Ak = float(input("Enter Ak:"))

    print("\nVector B")
    Bi = float(input("Enter Bi:"))        #Ai, Aj, Ak, Bi, Bj, Bk
    Bj = float(input("Enter Bj:"))
    Bk = float(input("Enter Bk:"))
    a = [Ai, Aj, Ak]
    b = [Bi, Bj, Bk]
    ans = nu.cross(a, b)
    s = str(ans[0]) + "i + " + str(ans[1]) + "j + " + str(ans[2]) + "k"
    x = "The vector product of A and B: " + s
    return x


if option.lower()=="scalar product" or option.lower()=="dot product":
           print(ScalarProduct())
else:
    if option.lower()=="vector product" or option.lower()=="cross product":
          print(VectorProduct())
    else:
        exit()

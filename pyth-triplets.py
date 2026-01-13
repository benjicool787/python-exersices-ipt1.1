#!/usr/bin/env python3
import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

if a*a + b*b == c*c:
    print(f"{a}, {b} und {c} sind ein pythagoräisches Triplet!")
else:
    print(f"{a}, {b}, und {c} sind kein pythagoräisches Triplet!")


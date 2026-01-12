#!/usr/bin/env python3

import sys
import math


r = float(sys.argv[1])


area = math.pi * r ** 2
circumference = 2 * math.pi * r


print(f"A={area:.2f}")
print(f"U={circumference:.2f}")

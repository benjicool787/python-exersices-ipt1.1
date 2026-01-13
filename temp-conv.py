#!/usr/bin/env python3

import sys 

temp = float(sys.argv[1])
unite = sys.argv[2]

if unite == 'F' or unite == 'f':
    c = (temp-32) * 5/9
    print(f"{temp}°F = {c:.1f}°C")
elif unite == 'C' or unite == 'c':
    f = temp * 9/5 + 32
    print(f"{temp}°C = {f:.1f}°F")

#!/usr/bin/env python3

import sys 

betrag = float(sys.argv[1])
waehrung = sys.argv[2]

if waehrung == "USD":
    chf = betrag * 0.80
elif waehrung == "EUR":
    chf = betrag * 0.93
elif waehrung == "GBP":
    chf = betrag * 1.07

    print(f"CHF {chf:.2f}")    



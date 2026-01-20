#!/usr/bin/env python3
import sys

buchstabe = sys.argv[1].lower()

match buchstabe:
    case "a" | "e" | "i" | "o" | "u":
        print(f"'{buchstabe}' ist ein Vokal")
    case "b" | "c" | "d" | "f" | "g" | "h" | "j" | "k" | "l" | "m" | \
         "n" | "p" | "q" | "r" | "s" | "t" | "v" | "w" | "x" | "y" | "z":
        print(f"'{buchstabe}' ist ein Konsonant")
    case _:
        print(f"'{buchstabe}' ist unbekannt")


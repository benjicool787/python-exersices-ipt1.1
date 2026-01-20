#!/usr/bin/env python3
import sys
import random

spieler = sys.argv[1].lower()

computer_zahl = random.randint(0, 2)

if computer_zahl == 0:
    computer = "rock"
elif computer_zahl == 1:
    computer = "paper"
else:
    computer = "scissors"

print(f"Spieler: {spieler.capitalize()}")
print(f"Computer: {computer.capitalize()}")

if spieler == computer:
    print("Unentschieden!")
elif (
    (spieler == "scissors" and computer == "paper") or
    (spieler == "paper" and computer == "rock") or
    (spieler == "rock" and computer == "scissors")
):
    print("Der Spieler gewinnt!")
else:
    print("Der Computer gewinnt!")

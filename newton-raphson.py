#!/usr/bin/env python3

import sys


epsilon = 0.001 # required accuracx
x = float(sys.argv[1])

guess = x/2.0

while abs(guess**2 - x) >= epsilon:
    guess = guess - ((guess**2 - x)/(2*guess))

print(guess)

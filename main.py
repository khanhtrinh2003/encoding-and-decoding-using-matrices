import numpy as np
from sympy import *
from encode_decode import decode, encode

i = int(input("press 1 (encode), 2 (decode): "))

if i == 1:
	encode(input("enter sentence "))

elif i == 2:
	e=input("Enter entries separated by space: ")
	decode(e)

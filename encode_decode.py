import numpy as np
from sympy import *

maso = {' ': 0, 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26,
      0: ' ', 1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'          
     }

#key for decode, inverse matrix 
kom = Matrix([[1,6,0], [2,2,0], [0,3, 5]])
inve = kom**-1

def decode(e):
    # single line separated by space
    entries = list(map(int, e.split()))

    while (len(entries)%3 != 0):
        entries.append(0)

    #create matrix
    me = Matrix(int(len(entries)/3), 3, entries)*inve

    #turn all elements of matrix into a list
    b = list(me)

    # convert all elements of list b into a sentence 
    c = []
    try:
        for i in range(len(b)):
            x = maso[b[i]]
            c.append(x)                       
        separator = ''
        print(separator.join(c)) 
    except:
        print('Matrix is invalid')

def encode(me):
    b=[]

    #convert to list of number
    for i in range(len(me)):
        x = maso[me[i]]
        b.append(x)  

    while (len(b)%3 != 0):
        b.append(0)

    #convert to matrix
    re = np.dot(Matrix(int(len(b)/3), 3, b), kom)
    print(re)

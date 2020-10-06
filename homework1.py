#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 13:25:54 2020

@author: matthias

Homework 1
"""

import numpy as np


"""
Example 1
"""

a = 63
print('type of a is ', type(a))

b = 42.0 
print('type of b is ', type(b))

c = '127.32'
print('type of c is ', type(c))

d = (True, False)
print('type of d is ', type(d))

e = 1 == 2
print('type of e is ', type(e))

f = dict([(1,'a'), (2,'b')])
print('type of f is ', type(f))


"""
Example 2
"""

a = 1 >= 3 or 2 < 3
print('a = ',a)

b = 63%4
print('b = ',b)

c = 63 // 2 <= 42
print('c = ',c)

d = np.array([1,2]*3)*3
print('d = ',d)



"""
Example 3
"""

def beer(bottles):
    """
    takes an integer 'bottles' counts down to 0 and sings verses
    """
    song = []
    startvalue = bottles
    
    if type(bottles) != int:
        raise TypeError("Only integers are allowed", type(bottles)) 
        
    else:
       for bottles in range(bottles,-1,-1):
           if bottles > 2:
               song.append("{} bottles of beer on the wall, {} bottles of beer, take one off, pass it around, {} bottles of beer on the wall!".format(bottles, bottles, bottles-1)) 
            
           if bottles == 2:
               song.append('{} bottles of beer on the wall, {} bottles of beer, take one off, pass it around, {} bottle of beer on the wall!'.format(bottles, bottles, bottles-1))
                   
           if bottles == 1:
               song.append('{} bottle of beer on the wall, {} bottle of beer, take one off, pass it around, no more bottles of beer on the wall!'.format(bottles, bottles))
                         
           if bottles == 0:
               song.append('No more bottles of beer on the wall, no more bottles of beer, go to the shop, by some more, {} bottles of beer on the wall!'.format(startvalue))
    return(song)
           
print(beer('a')) 
    
    



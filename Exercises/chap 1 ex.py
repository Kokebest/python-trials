# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 06:16:01 2021

@author: kokeb
"""

>>> # exercises from chapter 1
>>> print("wellcome to python")
wellcome to python
>>> print("welcome to computer science")
welcome to computer science
>>> print("programming is fun")
programming is fun
>>> print("programming is fun"\n)
SyntaxError: unexpected character after line continuation character
>>> print("programming is fun\n")
programming is fun

>>> print("programming is fun.\n programming is fun.\n programming is fun.\n programming is fun.\n programming is fun.\n")
programming is fun.
 programming is fun.
 programming is fun.
 programming is fun.
 programming is fun.

>>> print("FFFFFFF   U    U   NN    NN\nFF   U    U   NNN    NNN\nFFFFFFF\nFF\nFF)
	  
SyntaxError: EOL while scanning string literal
>>> print("FFFFFFF   U    U   NN    NN\nFF   U    U   NNN    NNN\nFFFFFFF\nFF\nFF")
	  
FFFFFFF   U    U   NN    NN
FF   U    U   NNN    NNN
FFFFFFF
FF
FF
>>> print("FFFFFFF   U    U   NN    NN\nFF        U    U   NNN    NNN\nFFFFFFF\nFF\nFF")
	  
FFFFFFF   U    U   NN    NN
FF        U    U   NNN    NNN
FFFFFFF
FF
FF
>>> print("FFFFFFF   U    U   NN    NN\nFF   U    U   NNN NNN\nFFFFFFF\nFF\nFF")
	  
FFFFFFF   U    U   NN    NN
FF   U    U   NNN NNN
FFFFFFF
FF
FF
>>> print("FFFFFFF   U    U   NN    NN\nFF        U    U   NNN    NNN\nFFFFFFF\nFF\nFF")
	  
FFFFFFF   U    U   NN    NN
FF        U    U   NNN    NNN
FFFFFFF
FF
FF
>>> print("FFFFFFF   U    U   NN    NN\nFF        U    U   NNN  NNN\nFFFFFFF    U    U   NN    NN\nFF\nFF")
	  
FFFFFFF   U    U   NN    NN
FF        U    U   NNN  NNN
FFFFFFF    U    U   NN    NN
FF
FF
>>> print("FFFFFFF   U    U   NN    NN\nFF        U    U   NNN  NNN\nFFFFFFF   U    U   NNN     NNN\nFF\nFF")
	  
FFFFFFF   U    U   NN    NN
FF        U    U   NNN  NNN
FFFFFFF   U    U   NNN     NNN
FF
FF
>>> print("FFFFFFF   U    U   NN    NN\nFF        U    U   NNN  NN\nFFFFFFF    U    U   NN    NN\nFF\nFF")
	  
FFFFFFF   U    U   NN    NN
FF        U    U   NNN  NN
FFFFFFF    U    U   NN    NN
FF
FF
>>> print("FFFFFFF   U    U   NN    NN\nFF       U    U   NNN   NN\nFFFFFFF   U    U   NN N     NN\nFF       U  U    NN  N   NN\nFF")
	  
FFFFFFF   U    U   NN    NN
FF       U    U   NNN   NN
FFFFFFF   U    U   NN N     NN
FF       U  U    NN  N   NN
FF
>>> print("FFFFFFF   U    U   NN    NN\nFF        U    U   NNN   NN\nFFFFFFF   U    U   NN N     NN\nFF         U  U    NN  N   NN\nFF")
	  
FFFFFFF   U    U   NN    NN
FF        U    U   NNN   NN
FFFFFFF   U    U   NN N     NN
FF         U  U    NN  N   NN
FF
>>> print("FFFFFFF   U    U   NN    NN\nFF        U    U   NNN   NN\nFFFFFFF   U    U   NN N     NN\nFF         U  U    NN  N  NN\nFF")
	  
FFFFFFF   U    U   NN    NN
FF        U    U   NNN   NN
FFFFFFF   U    U   NN N     NN
FF         U  U    NN  N  NN
FF
>>> print("FFFFFFF   U    U   NN    NN\nFF        U    U   NNN   NN\nFFFFFFF   U    U   NN N  NN\nFF         U  U    NN  N NN\nFF")
	  
FFFFFFF   U    U   NN    NN
FF        U    U   NNN   NN
FFFFFFF   U    U   NN N  NN
FF         U  U    NN  N NN
FF
>>> print("FFFFFFF   U    U   NN    NN\nFF        U    U   NNN   NN\nFFFFFFF   U    U   NN N  NN\nFF         U  U    NN  N NN\nFF    U    NN    NNN")
	  
FFFFFFF   U    U   NN    NN
FF        U    U   NNN   NN
FFFFFFF   U    U   NN N  NN
FF         U  U    NN  N NN
FF    U    NN    NNN
>>> print("FFFFFFF   U    U   NN    NN\nFF        U    U   NNN   NN\nFFFFFFF   U    U   NN N  NN\nFF         U  U    NN  N NN\nFF       U    NN    NNN")
	  
FFFFFFF   U    U   NN    NN
FF        U    U   NNN   NN
FFFFFFF   U    U   NN N  NN
FF         U  U    NN  N NN
FF       U    NN    NNN
>>> print("FFFFFFF   U    U   NN    NN\nFF        U    U   NNN   NN\nFFFFFFF   U    U   NN N  NN\nFF         U  U    NN  N NN\nFF           U    NN    NNN")
	  
FFFFFFF   U    U   NN    NN
FF        U    U   NNN   NN
FFFFFFF   U    U   NN N  NN
FF         U  U    NN  N NN
FF           U    NN    NNN
>>> print("FFFFFFF   U    U   NN    NN\nFF        U    U   NNN   NN\nFFFFFFF   U    U   NN N  NN\nFF         U  U    NN  N NN\nFF           U     NN    NNN")
	  
FFFFFFF   U    U   NN    NN
FF        U    U   NNN   NN
FFFFFFF   U    U   NN N  NN
FF         U  U    NN  N NN
FF           U     NN    NNN
>>> print("FFFFFFF   U    U   NN    NN\nFF        U    U   NNN   NN\nFFFFFFF   U    U   NN N  NN\nFF         U  U    NN  N NN\nFF           U     NN    NN")
	  
FFFFFFF   U    U   NN    NN
FF        U    U   NNN   NN
FFFFFFF   U    U   NN N  NN
FF         U  U    NN  N NN
FF           U     NN    NN
>>> 

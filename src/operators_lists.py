#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 2, 2014

@author: anroco

How working operators + and * with lists in python?

¿como funcionan los operadores + y * con las listas en python?
'''

#create a list
lista = ['hello']
print (lista)

#The * operator allow repeat the items in the list
print(lista * 5)

#create a list with repeated items.
lista = [1, 2, 3] * 3
print(lista)

#create two list
lista1 = ['a', 'b', 'c', 'd']
lista2 = ['e', 'd', 'e', 'f']
lista3 = ['g', 'h', 'i']

#The + operator allow create a list joining two or more lists
lista = lista1 + lista2 + lista3
print(lista)

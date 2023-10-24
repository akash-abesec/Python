# """
#                                      DATA TYPES
# :Numeric
#    Integers
#    Float
#    Complex Numbers
# :Sequence Type
#    String
#    List
#    Tuple
# :Dictionary
# :Set
#
#
#
# :mutable object can change its state or contents and immutable objects cannot.
#        Mutable Data Types
# Dictionary
# list
# byte array
#        Immutable Data types
# int
# float
# string
# tuple
# set
#
# Integers
# Float
# Complex numbers
# a=5 print(a,"is of type",type(a))  #5 is of type<class 'int'>
# a=2.0 print(a,"is of type",type(a)) #2.0 is of type<class 'float'>
# a=1+2j print(a,"is of type",type(a)) #is of type <class 'complex'>
#
# a=5
# print(a,type(a))
# b=3.4
# print(b,type(b))
# c=1+3j
# print(c,type(c))
#
#                                 String
# A string is a collection of one or more character put in a single quota,double-quota or triple quote
# Multi-line strings can be denoted using triple quotes,(''')or""""""
#
# s="This is a string"
# print(s)
# s='''A multiline string'''
# print(s)
# a='Hello@123'
# print(a,type(a))
# b='''
# Hello
# welcome to python
# '''
# print(b)
# s='10'
# print(s,type(s))
#                          List
# List is an ordered sequence of items.
# It is one of the most used datatype in python and is very flexible.
# [].
#
# a=[1,2.2,'ws']
#
# l=[10,'ws',5.5]
# print(l,type(l))
# l[2]=10
# print(l)
#
#                                Tuple
# Tuple is an ordered sequence of items same as a list.
#  It is defined within parentheses () where items are separated by commas.
# for example :-t=(5,'program',1+3j)
# t=(1,'akash singh',2+4J)
# print(t,type(t))
# T=(2)
# print(T,type(T))
#                              Directory
# Directory is an unordered collection of key-value paires.
# In Python ,dictionary are defined within braces {} with each item being a pair in the form key:value
# For example:-
# d={1:'value','key':2}
# print(type(d))
# D={
#     'course_name':'Python',
#     'course_duration':'2 Month'
# }
# print(D,type(D))
#                                     Set
# A set is an unordered collection of items.
# Every set element is unique (no duplicates) and must be immutable (cannot be changed).
# {}
# For example:-
# my_set={1,2,3}
# print(my_set,type(my_set))
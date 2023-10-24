"""
Python String Function
lower()
upper()
title()
capitalize()
find()
index()
isalpha()
isdigit()
isalnum()
chr()=This takes in an integer i and converts it to a character c,so it returns a character string.

              #Convert integer 65 to ASCII Character ('A')
              y=chr(65)
              print(type(y),y)         #Output=<class'str'>A
ord()=This takes a single Unicode character (string of length 1) and returns an integer , so the format is:
#Converts ASCII Unicode Character 'A' to 65
y=ord('A')
print(type(y),y)
<class'int'>65

w="Welcome To Ws cube tech"
n=w.lower();
print(n)

u=w.upper()
print(u)

v=w.title()
print(v)

x=w.capitalize()
print(x)

w="Welcome23"
print(w.find('e',2))

print(w.index('e',3))

print(w.isalpha())

print(w.isdigit())

print(w.isalnum())

a=65;
print(chr(a))

h='C'
print(ord(h))

"""
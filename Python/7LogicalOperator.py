"""
Operator                   Description                                 Example
and                Returns True if both statements are True         x<5 and x<10
or                 Returns True if one of the statements are True   x<5 or x<4
not         Reverse the result,returns False if the result is True    not(x<5 and x<10)
"""
x=10
y=20

print(x==10 and x<y and x==y)
print(x==10 or x<y or x==y)
print(not x!=10)
"""
Operator             Name            Description
&                    AND               x&y
|                    OR                 x|y
^                    XOR                 x^y
"""
"""
                 1=true        0=False
 A           B            A&B            A|B       A^B
 0           0            0               0         0
 0           1            0               1         1
 1           0            0               1         1
 1           1            1               1         0

x=10
y=8
print(bin(x))
print(bin(y))
print(x&y,bin(x&y))
print(x|y,bin(x|y))
print(x^y,bin(x^y))"""
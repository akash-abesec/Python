"""
list :- mutable,[],seperated by comma ,
Multiple value

"""
l=[1,2,3,4,[5,6,7],"Akash","School"]
print(type(l))
print(l[4])
l.insert(3,4)  # insert 4 at index of 3
print(l)
l.pop(4)
print(l)
l.reverse()
print(l)
l.append(1)
print(l)
l.reverse()
print(l[0 : ])     #start from 0 to end of list
for i in l:
    print(i)
k=[1,2,3,4,5,6]
print(k[-1: :-1])  #reverse printing( start:end:increament or decrement)



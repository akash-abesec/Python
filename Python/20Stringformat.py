"""
named indexes:
"""
txt1 = "Welcome to {fname}{lname}".format(fname="WsCube",lname=" Tech")
print(txt1)
"""
numbered indexes:
"""
txt2="Welcome to {0} {1}".format("WsCube","Tech")
print(txt2)
"""
empty placeholders:
"""
txt3="Welcome to {} {}".format("Wscube","Tech")
print(txt3)
t="Welcome {1} to {0} WsCube Tech".format("Hello",20)
print(t)

w="Welcome {b:>10} to {a} Wscubetech".format(a=30,b=40)
print(w)


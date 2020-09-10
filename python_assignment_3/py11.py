import random
x = open("test.txt")
y=x.read()
lst=y.splitlines()
z=random.choice(lst)
print(z)
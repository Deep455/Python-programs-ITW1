print("program-1 : ")
a=5
b=2
try:
    print(a/b)
except:
    print("some error")
else:
    print("no error")
finally:
    print("finished")
print()

print("program-2 : ")
a=5
b=0
try:
    print(a/b)
except:
    print("some error")
else:
    print("no error")
finally:
    print("finished")
print()

print("program-3")
a=5
b=0
if b==0:
    raise Exception("You can't divide by zero")
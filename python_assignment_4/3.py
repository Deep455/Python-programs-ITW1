class A:
    pass

class B(A):
    pass

class C(B):
    pass

print(issubclass(B,A))
print(issubclass(C,A))
print(issubclass(A,B))
print(issubclass(A,C))
print(issubclass(C,B))
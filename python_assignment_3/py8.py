import os
x = os.stat("test.txt")
size = x.st_size
print("size of file is {} bytes".format(size))
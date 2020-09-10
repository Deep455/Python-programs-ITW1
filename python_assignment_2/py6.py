lst = ((2, "w"),(3, "r"),(12, "m"),(4, "x"),(5, "z"),(7, "a"),(32, "s"),(45, "d"),(23, "b"),(19, "y"))
print("initially we have : ")
print(lst)
lst=dict(lst)
lst = { y : x for x,y in lst.items()}
print("After update we have : ")
print(lst)
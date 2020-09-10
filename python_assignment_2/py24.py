import random
import string

n = 100
lst=[]
for i in range(n):
    ticket = ''.join(random.choices(string.digits, k = 10))
    lst.append(ticket)
print(lst)

lucky1 = ''.join(random.choices(lst))
lucky2 = ''.join(random.choices(lst))

print(lucky1,lucky2)
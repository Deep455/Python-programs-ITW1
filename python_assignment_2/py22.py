import random 
import string 
   
pwd1 = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k = 10)) 
pwd2 = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k = 10))
pwd3 = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k = 10))

print("first random string : " + str(pwd1))
print("first random string : " + str(pwd2))
print("first random string : " + str(pwd3))
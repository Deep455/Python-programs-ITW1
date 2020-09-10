from itertools import permutations  
def Permutation_and_combination(string): 
    permutation_list = permutations(string)
    print("All possible permutations are : ")
    for x in permutation_list:
        print (''.join(x))

string=input("Enter the string : ")
Permutation_and_combination(string)
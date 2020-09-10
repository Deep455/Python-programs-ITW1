class pro:
    string=""
    def rev(self,s):
        self.string=s
        new_string=""
        for x in self.string:
            new_string = x + new_string
        return new_string

string=input("enter a string : ")
a=pro()
new_string=a.rev(string)
print("reversed string : " + new_string)
def decoration(string):
    string = bold(string)
    string = italic(string)
    string = underline(string)
    return string

def bold(string):
    BOLD='\033[1m'
    string = BOLD + string
    return string
def italic(string):
    ITALIC = '\033[3m'
    string = ITALIC + string
    return string
def underline(string):
    UNDERLINE = '\033[4m'
    string = UNDERLINE + string
    return string

string = input("enter a string : ")
string = decoration(string)
print(string)
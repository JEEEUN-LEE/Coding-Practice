import re 

n = int(input())        
pattern = input()  

regex_pattern = "^" + pattern.replace("*", ".*") + "$"

for _ in range(n):
    filename = input()

    if re.match(regex_pattern, filename):
        print("DA")
    else:
        print("NE")

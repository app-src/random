s="aditya"
# s=s.upper()
print("\n\n\n")
for i in range(len(s)-1):
    print((len(s)-i+10)*" "+s[:i]+"["+s[i].lower()+"]"+s[i+1:])
print("\n\n\n")
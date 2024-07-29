s = input()

k = s[0]

new = 0
value = "False"
m = 0
if s[0] == s[0].lower() and s.isalpha():
    m += 1
    for i in range(0,len(s)):
        if s[i-1] == s[i-1].upper():
            new += 1
            value = "True"
else:
    value = "False"



if value == "False":
    print(value)
else:
    theValue = int(new)+int(m)
    print(value,theValue)

import re
a = input()
the_checking = re.sub(r"[^a-zA-Z0-9]", "", a).lower()
print(the_checking == the_checking[::-1])

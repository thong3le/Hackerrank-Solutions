import re
s = raw_input()

print True if (re.search(r"^M{0,5}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$", s)) else False
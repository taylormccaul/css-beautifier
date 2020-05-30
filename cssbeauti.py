import re

with open("messy.css", "r") as f:
    for line in f:
        line = re.sub("\s*{\s*", " {\n", line)
        line = re.sub("\s*}\s*", "\n}\n\n", line)
f.close()

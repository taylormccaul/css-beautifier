import re

with open("messy.css", "r") as f:
    for line in f:
        line = re.sub("\s*{\s*", " {", line)
        for m in re.finditer("\w+\s*{\s*", line):
            line = line.replace(line[m.start():m.end()], m.group() + "\n")
        print(line)
f.close()

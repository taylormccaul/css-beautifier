import re

with open("messy.css", "r") as f:
    for line in f:
        for m in re.finditer("{", line):
            #print("%02d-%02d: %s" % (m.start(), m.end(), m.group()))
            print(re.sub("\s*{", " { ", line))
            #print(line.replace(line[m.start():m.end()], m.group() + "\n"))
            #line = line.replace(line[m.start():m.end()], m.group() + "\n")
f.close()

import re

with open("messy.css", "r") as f:
    for line in f:
        line = re.sub("\s*{\s*", " {\n", line)
        line = re.sub("\s*}\s*", "\n}\n\n", line)
        line = re.sub(";\s*\s*", ";\n", line)
        """for m in re.finditer(";\s*[A-Za-z]+\s*[\n]{0}", line):
            y = m.start()
            z = m.end()
            print(line[y])
            print(line.replace(line[y], ";\nS"))
            #line = line.replace(line[y:y+1], ";\n")
            #print(line.replace(line[y:y+1], ";\n"))
            #print(line.strip())"""
        print(line)
f.close()

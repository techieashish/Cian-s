f = open("./fields.txt", "r")
fields = []
for line in f.readlines():
    fields.append(line.split("=")[0].rstrip(" ").lstrip(" ").strip(" "))
print(fields)
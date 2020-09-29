with open("compliments.txt", "r") as f:
    file = f.read()

lines = file.split("\n")

print(lines)

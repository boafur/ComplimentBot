# This script will output all items in a text file in list format
# Please create a file called `compliments.txt` and then put each compliment on a new line.
f = open("compliments.txt", "r")

output = [line.rstrip('\n') for line in f]

f.close()

print(output)

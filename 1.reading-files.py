#open the file
handle = open("./data/quotes.txt","r")

#create a dictionary
counts = dict()

#read the file: line by line
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = 1 + counts.get(word,0)

print(counts)
# Ref:
# Dictionary : https://www.geeksforgeeks.org/python-dictionary/

p = open("data.txt","r")
text=p.read()
text = text.lower()

words = text.split()
Frequency = {}

for word in words:
    if word in Frequency:
        Frequency[word]+=1
    else:
        Frequency[word]=1

print("Frequencies of words in file :\n")
for word , count in Frequency.items():
    print(f"{word}:{count}")
 
fin=open('words.txt')
for line in fin:
    word=line.strip()
    if len(word)>5:
        print(word)

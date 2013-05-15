def has_no(n,e):
    for i in e:
        for letter in n:
            if letter == i:
                return False
    return True
            


t=input('PLease enter forbidden no')

fin=open('words.txt')
for line in fin:
    word=line.strip()
    r=has_no(word,t)
    if r==True:
        print(word)

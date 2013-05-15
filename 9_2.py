def has_no_e(n):
    for letter in n:
        if letter == 'e':
            return False
    return True
            
fin=open('words.txt')
for line in fin:
    word=line.strip()
    r=has_no_e(word)
    if r==True:
        print(word)

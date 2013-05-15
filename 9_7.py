def check(word):
    r=len(word)
    i=0
    z=0
    if r>5:
        while r>1:
            #print(r)
            if word[i]==word[i+1]:
                r=r-2
                i=i+2
                z=z+1
                if z>1:
                    return True
                #print("equal")
            else:
                #print("not equal")
                r=r-1
                i=i+1
                z=0
        #print(z)
        
    else:
        #print("cannot possible")
        return False
def equal(word,j):
    if word[j]==word[j+1]:
        return True


count=0
f=open("englishword.txt")
'''
k="bookkeeper"
if check(k)==True:
    print(k)

'''
q=0

for line in f:
    k=line.strip()
    #k=f.readline()
    if check(k)==True:
        print(k)
    else:
        q=q+1

print("total no of words checkedL:",end="")
print(q)



'''
Task: take input from file and convert into list word by word
by slash
python 3.3
'''
k=[]
q=open("line.txt")
w=q.readlines()
for i in range(0,len(w)):
    f=w[i]
    f=f.strip()
    while True:
        r=f.find(' ')
        if r<0:
            z=f
        else:
            z=f[0:r]
        f=f[r+1:]
        #print(r)
        f.strip()
        k.append(z)
        if r<0:
            break;
print(k)

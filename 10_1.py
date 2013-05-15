def sumlist(lon):
    new=[]
    for i in range(0,len(lon)):
        new.append(sum(lon[0:i+1]))
    print(new)

s=[1,2,7,5]
sumlist(s)

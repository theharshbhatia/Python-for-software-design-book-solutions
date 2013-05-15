def remove_duplicates(lost):
    lost.sort()
    k=0
    for i in range(0,len(lost)-1):
        print(i+1)
        if lost[i]==lost[i+1]:
            lost[i]='0'
            k=k+1
    for i in range(0,k):
        lost.remove('0')
    return lost

s=['h','a','r','r','h','h','r']
print(remove_duplicates(s))

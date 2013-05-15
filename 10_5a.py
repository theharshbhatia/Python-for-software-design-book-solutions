def has_duplicates(lost):
    lost.sort()
    for i in range(0,len(lost)-1):
        if lost[i]==lost[i+1]:
            return True

s=['h','a','r','s','h']
print(has_duplicates(s))

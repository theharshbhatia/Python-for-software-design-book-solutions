def arc(m,n):
    if m==0:
        return n+1
    else:
        if m>0:
            if n==0:
                return arc(m-1,1)
            else:
                if n>0:
                    return arc(m-1,arc(m,n-1))
            
r=arc(3,4)
print(r)

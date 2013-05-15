def gcd(a,b):    
    if b==0:
        print("gcd is equal to",a)        
    else:
        r=a%b
        return gcd(b,r)


gcd(25,125)

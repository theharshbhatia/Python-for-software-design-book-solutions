def rotate_word(s,n):
    for i in range(0,len(s)):
        n=int(n)
        k=ord(s[i])
        if k>64 and k<91:
            k=ord(s[i])+ n
            if k>90:
                k=65+(k-90)                
        else:
            if k >96 and k<123:
                k=ord(s[i])+ n
                if k>122:
                    k=97+(k-122)
        print(chr(k),end="")

rotate_word('Cheer','7')

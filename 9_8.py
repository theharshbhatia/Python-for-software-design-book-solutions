def odometer_palindrome(digit):
    q=len(digit)
    h=q/2
    h=int(h)
    q=q
    i=0
    r=1
    rev=digit[::-1]
    print(digit[i+r:h])
    print(rev[i+r:h])
    if digit[i:h]==rev[i+r:h+r]:
        print(q-r,"letter palindrome")
    else:
        print("nothing")

digit="612145"
print(odometer_palindrome(digit))

#front palindrome : digit[i:h]==rev[i+r:h+r]

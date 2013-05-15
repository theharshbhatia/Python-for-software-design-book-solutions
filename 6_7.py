def is_divisible(a,b):
    if a%b == 0:
        return 'true'
    else:
        return 'false'

def power(a,b):
    c = a/b
    d=c/b
    if d==b or d==1:
        return 'true'
    else:
        return 'false'

def is_power(a,b):
    r=is_divisible(a,b)
    v=power(a,b)
    if r=='true':
        if v=='true':
            print('a is power of b')
        else:
            print('a is divisible by b but not power of b')
    else:
        if r=='false':
            print('a is nor divisible nor power of b')
        

is_power(7,4)

def straight():
    print ('-------',end="")

def mid():
    print ('|')

def space():
    print('|       ',end="")

def plus():
    print("+",end="")

def plusend():
    print("+")

def first():
    plus()
    straight()
    plus()
    straight()
    plusend()

def second():
    space()
    space()
    mid()

def draw(n,m):
    for i in range(0,n):
        first()
        for j in range(0,m):
            second()
                  
    first()
    
    
draw(2,3)
    



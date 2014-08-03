'''
Complete soltion of Book 
"Python For Software Design by Allen B. Downey"
by Harsh Bhatia ( www.harshbhatia.net )
'''
'''
Exercise: 6.3
'''

def is_between(x,y,z):
  if x<=y:
    if y<=z:
      return "True"
    else:
      return "False"
  else:
    return "False"

print is_between(3,4,2)

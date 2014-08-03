'''
Complete soltion of Book 
"Python For Software Design by Allen B. Downey"
by Harsh Bhatia ( www.harshbhatia.net )
'''
'''
Exercise 7.1: Rewrite the function print_n from Section 5.8 using iteration instead of recursion.
'''
def print_n(s, n):
  while n != 0:
    print s
    n=n-1
  
print_n(2,7)
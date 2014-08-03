'''
Complete soltion of Book 
"Python For Software Design by Allen B. Downey"
by Harsh Bhatia ( www.harshbhatia.net )
'''
'''
Exercise: 6.6: incomplete
'''
def first(word):
  return word[0]

def last(word):
  return word[-1]

def middle(word):
  return word[1:-1]

print middle("aa")
print middle("b")
print middle('')

def is_palindrome(word):
  wordl=int(len(word))
  if (wordl%2==0):
    print "even"
  else:
    for i in wordl:
      if word[i]==word[-i]:
        return 0
      else:
        return 1

print is_palindrome("lol")
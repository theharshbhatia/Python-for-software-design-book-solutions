def is_anagrams(let1,let2):
    if len(let1)==len(let2):
        if sorted(let1)==sorted(let2):
            return True
        else:
            return False
    else:
        return False
l='abrss'
l1='abssr'
print(is_anagrams(l,l1))

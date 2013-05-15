def uses_all(word,test):
    for t in test:        
        if t not in word:
            return False
    return True

print(uses_all('heeeeel','he'))

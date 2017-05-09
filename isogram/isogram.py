import collections

def is_isogram(word):
    
    word = word.lower()
    word = ''.join(filter(str.isalpha, word))
    
    d = collections.defaultdict(int)
    for c in word:
        d[c] += 1 
    
    for c in word:
        if d[c]>1:
            return False

    return True

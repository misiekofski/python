def detect_anagrams(anagram, word_list):
    letters = sorted(anagram.lower())
    return [word for word in word_list
            if sorted(word.lower()) == letters
            and word.lower() != anagram.lower()]

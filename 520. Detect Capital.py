def detectCapitalUse(word: str) -> bool:
    #all caps
    if word.upper() == word:
        return True

    #all lower
    if word.lower() == word:
        return True

    if word[1:].lower() == word[1:] and word[0] == word[0].upper():
        return True
    
    return False
def word_count(book):
    formatted = book.split()
    return len(formatted), formatted

def character_count(book):
    counts = dict()
    lower = book.casefold()
    for letter in lower:
        if (not letter.isalpha()):
            continue
        elif (counts.get(letter) == None):
            counts.update({letter: 1})
        else:
            counts.update({letter: counts[letter] + 1})
    
    return counts
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

def report_dict(char_counts):
    character_list = []
    for c in char_counts:
        character_list.append({'char': c, 'count': char_counts[c]})
    character_list.sort(reverse=True, key=lambda x: x['count'])
    return character_list
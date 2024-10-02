def main():
    split_book = process_book('books/frankenstein.txt')
    counted = character_count(split_book)
    book_report(dict_to_list(counted))

def sort_by_num(dict):
    return dict['count']

def process_book(path_to_book):
    with open(path_to_book, 'r') as file:
        current_book = file.read()
        formatted = current_book.lower()
        letters = [c for c in formatted]
        return letters
        # print(letters)
        # print(len(word_split))

def character_count(book):
    counts = dict()
    for letter in book:
        if (not letter.isalpha()):
            continue
        elif (counts.get(letter) == None):
            counts.update({letter: 1})
        else:
            counts.update({letter: counts[letter] + 1})
    
    return counts

def dict_to_list(d):
    converted = []
    for x in d:
        converted.append({'letter': x, 'count': d[x]})
    converted.sort(reverse=True, key=sort_by_num)
    return converted
    

def book_report(char_counts):
    for char in char_counts:
        print(f"The '{char.get('letter')}' character was found {char.get('count')} times.")
    
main()

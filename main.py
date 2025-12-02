import sys
from stats import *

def main():
    #split_book = process_book('books/frankenstein.txt')
    #counted = character_count(split_book)
    #book_report(dict_to_list(counted))
    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = get_book_text(sys.argv[1])
    words, formatted = word_count(book)
    characters = character_count(book)
    print(f"Found {words} total words")
    report = report_dict(characters)
    for r in report:
        print(f"{r['char']}: {r['count']}")
    #print(report)
    #print(formatted)

def sort_by_num(dict):
    return dict['count']

def get_book_text(path_to_book):
    with open(path_to_book, 'r') as file:
        current_book = file.read()
        return current_book

def process_book(path_to_book):
    with open(path_to_book, 'r') as file:
        current_book = file.read()
        formatted = current_book.lower()
        letters = [c for c in formatted]
        return letters
        # print(letters)
        # print(len(word_split))

def dict_to_list(d):
    converted = []
    for x in d:
        converted.append({'letter': x, 'count': d[x]})
    converted.sort(reverse=True, key=sort_by_num)
    return converted
    
main()

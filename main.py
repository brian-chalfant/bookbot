
from stats import get_book_text, get_num_words, get_num_char,sort_dict
import sys


def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        filepath = sys.argv[1]
        text = get_book_text(filepath)
        word_count = get_num_words(text)
        sorted_list = sort_dict(get_num_char(text))
        print_report(filepath, word_count, sorted_list)


def print_report(filepath, word_count, sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"{word_count}")
    print("--------- Character Count -------")
    for line in sorted_list:
        print(f"{line["char"]}: {line["num"]}")
    print("============= END ===============")
main()
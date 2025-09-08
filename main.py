from stats import get_num_words, get_char_count, get_sorted_char_map
import sys

def get_book_text(file_path:str):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def main():

    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
    
    try:
        book_path = sys.argv[1]
        print('============ BOOKBOT ============')
        print(f'Analyzing book found at:', book_path)
        book_text = get_book_text(book_path)
        num_words = get_num_words(book_text)
        print('----------- Word Count ----------')
        print(f'Found {num_words} total words')
        char_map = get_char_count(book_text)
        sorted_char_map = get_sorted_char_map(char_map)
        print('--------- Character Count -------')
        for map in sorted_char_map:
            print(f'{map['char']}: {map['num']}')
    except FileNotFoundError:
        print('Usage: python3 main.py <path_to_book>')
    
    


if __name__ == "__main__":
    main()
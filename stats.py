def get_num_words(book_text:str):
    words = book_text.split()
    return len(words)

def get_char_count(book_text:str) -> dict:
    result = {}
    for c in book_text:
        curr_char = c.lower()
        if curr_char in result:
            result[curr_char] += 1
        else:
            result[curr_char] = 1
    return result

def get_sorted_char_map(char_map: dict) -> list:
    # {'b': 4868} -> {'char': 'b', 'num': 4868}
    result = [{'char': c, 'num': n} for c, n in char_map.items()]
    result.sort(reverse=True, key=sort_on)
    return result

def sort_on(items):
    return items['num']
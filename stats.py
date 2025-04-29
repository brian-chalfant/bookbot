def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def get_num_words(filecontents):
    words = filecontents.split()
    num_words = len(words)
    return f"Found {num_words} total words"

def get_num_char(filecontents):
    char_dict = {}
    for char in filecontents.lower():
        if char in char_dict.keys():
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(dict):
    return dict["num"]

def sort_dict(unsorted_dict):
    sorted_list = []
    for key in unsorted_dict.keys():
        if key.isalpha():
            temp_dict = {"char": key, "num": unsorted_dict[key]}
            sorted_list.append(temp_dict)
    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list

    
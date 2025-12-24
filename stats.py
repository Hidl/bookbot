def count_words(text):
    return len(text.split())

def count_characters(text):
    char_dict = {}
    chars = list(text.lower())
    for char in chars:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(items):
    return items["num"]

def sort_characters(char_dict):
    dict_list = []
    for entry in char_dict:
        if entry.isalpha():
            dict_list.append(
                {"character": entry, "num": char_dict[entry]}
            )
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
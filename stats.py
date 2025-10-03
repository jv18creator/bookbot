def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def count_characters(text):
    char_count = {}
    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count

def sort_on(items):
    return items["num"]

def sorted_characters(text):
    chars = count_characters(text)
    new_list = []
    for char in chars:
        num = chars[char]
        temp_dict = { "char": char, "num": num }
        if char.isalpha():
            new_list.append(temp_dict)


    new_list.sort(reverse=True, key=sort_on)

    return new_list
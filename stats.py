def get_num_words(text):
    words = text.split()
    total_words = len(words)
    return total_words

def get_character_count(text):
    text = text.lower()
    char_count = {}
    
    for char in text:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    
    return char_count

def get_sorted_chars(char_count):
    chars_list = []
    for char, count in char_count.items():
        chars_list.append({"char": char, "count": count})
    
    def sort_on(dict):
        return dict["count"]

    chars_list.sort(reverse=True, key=sort_on)

    return chars_list
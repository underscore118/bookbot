def get_number_words(text):
    words = []
    words = text.split()
    return len(words)

def get_chars_dict(text):
    char = {}
    for c in text:
        lowered = c.lower()
        if lowered in char:
            char[lowered] += 1
        else:
            char[lowered] = 1 
    return char



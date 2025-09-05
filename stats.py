#calcola il numero di parole
def get_number_words(text):
    words = []
    words = text.split()
    return len(words)

#conta quante volte appaiono ogni carattere nel testo
def get_chars_dict(text):
    char = {}
    for c in text:
        lowered = c.lower()
        if lowered in char:
            char[lowered] += 1
        else:
            char[lowered] = 1 
    return char


#crea il report
def get_report(charCount):
    splitChart = []
    for char, num in charCount.items():
        splitChart.append({"char" : char, "num" : num})  

    splitChart.sort(key=sort_on, reverse= True)

    return splitChart


def sort_on(item):
    return item["num"]
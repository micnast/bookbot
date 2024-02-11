with open("./books/Frankenstein.txt") as f:
    text = f.read()
    

def main():
    with open("./books/Frankenstein.txt") as f:
        dictionary_counts = letter_counts()
        print (dictionary_counts)

def word_count():
    words = text.split()
    return len(words)

def character_list():
    text_lower = text.lower()
    words = text_lower.split()
    full_letter_list = []
    for clusters in words:
        characters = [*clusters]
        full_letter_list += characters
    return(full_letter_list)

def letter_counts():
    possible_characters = []
    ticks = 0
    dictionary_counts = {}
    for characters in character_list():
        if characters in dictionary_counts:
            dictionary_counts[characters] += 1
        else:
            dictionary_counts[characters] = 1
    return dictionary_counts
                
         


main ()
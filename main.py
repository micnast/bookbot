file_to_open = "./books/Frankenstein.txt"
with open(file_to_open) as f:
    text = f.read()   
alphabet = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
def main():
    with open(file_to_open) as f:
        print (f"--- Begin report of books {file_to_open} ---")  
        print (f"{word_count()} words found in the document.")
        dictionary_counts = letter_counts()
        in_order = dictionary_to_list(dictionary_counts)
        in_order.sort(reverse=True, key=sort_on)
        for listed in in_order:
            if listed['character'] in alphabet:
                print (f"The '{listed['character']}' was found {listed['num']} times.")
        print ("--- End report ---")

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

def dictionary_to_list (dictionary_counts):
    listed_dictionary = [{"character": character, "num": count} for character, count in dictionary_counts.items()]
    return listed_dictionary

def sort_on (listed_dictionary):
    return listed_dictionary["num"]



main ()
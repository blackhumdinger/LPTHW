def break_words(stuff):
    """This function will break up words for us """
    words = stuff.split(' ')
    return words

def sort_words(words):
    """ this will sort the words for us """
    return sorted(words)


def print_first_words(words):
    """ prints the first word after popping it off """
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """ prints the last word after popping it off """
    word = words.pop(-1)
    print(word)
def sort_sentence(sentence):
    """ takes in full sentence and returns the sorted words """
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """  prints first and last word of a sentence"""
    words = break_words(sentence)
    print_first_words(words)
    print_last_word(words)
    

def print_first_and_last_sorted(sentence):
    """ sorts the words and prints the first and the last one """
    words = sort_sentence(sentence)
    print_first_words(words)
    print_last_word(words)
    

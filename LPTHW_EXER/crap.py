def break_words(stuff):
    """This function will break up words for us """
    words = stuff.split(' ')
    return words

sentence = "this is the best day of my life"

k = break_words(sentence)
print(k)
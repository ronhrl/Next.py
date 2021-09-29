def translate(sentence):
    words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}
    list_word = sentence.split(' ')
    new_str = ''
    new_generator = (words.get(word) for word in list_word)
    for new_word in new_generator:
        new_str = new_str + new_word + ' '
    return new_str


print(translate("el gato esta en la casa"))

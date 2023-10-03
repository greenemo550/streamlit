def replace_word_in_sentence(word):
    re_sentence = word.replace("apple", "mango")
    return re_sentence

sentence = "I have an apple. She has an apple. We all have apples."

print(replace_word_in_sentence(sentence))
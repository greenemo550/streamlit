def find_word_position(sentence, word):
    # この部分を完成させてください
    find_word = sentence.find(word)
    if not word == -1:
        return find_word
    return -1

sentence = "apple, banana, cherry, date, fig, grape"
print(find_word_position(sentence, "date"))  # 期待する出力: 23

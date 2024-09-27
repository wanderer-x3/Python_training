
def single_root_words(root_word, *other_words):

    root_word = root_word.lower()
    same_words = list()
    
    for i in other_words:
        s = i.lower()
        j = s.count(root_word)
        if j == 1:
            same_words.append(i)
        j = root_word.count(s)
        if j == 1:
            same_words.append(i)

    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)

# ['richiest', 'orichalcum', 'richies']
# ['Able', 'Disable']
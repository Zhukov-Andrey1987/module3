
def single_root_words(root_word, *other_words):
    print(f'Вы ищите слово: {root_word}, в списке слов: {other_words}')
    same_words = []
    for i in other_words:
        if i.count(root_word) != 0:
            same_words += [i]
    print(f'Подходят следующие слова {same_words}')


single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
print('_____________________________________________________________________')

def single_root_words(root_word, *other_words):
    print(f'Из списка: {other_words}, в  слове: {root_word} ,содрежатся следующие слова:')
    same_words = []
    for i in other_words:
        if root_word.lower().count(i.lower()) != 0:
            same_words += [i]
    print(same_words)


single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

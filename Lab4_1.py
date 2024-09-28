def get_count_char(str_):
    s=str_.lower()
    dict = {}
    for i in s:
        if i.isalpha():
            if i in dict.keys():
                number = dict[i]
                number+=1
                dict[i] = number
            else:
                dict[i] = 1

    return dict




main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))

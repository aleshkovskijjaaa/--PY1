from pprint import pprint
# TODO решить с помощью list comprehension и распечатать его
spisok = []
for i in range(16):
    dict_one = {'bin':bin(i), 'dec' : i, 'hex':hex(i), 'oct':oct(i)}
    spisok.append(dict_one)

pprint(spisok)

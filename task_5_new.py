from pprint import pprint
# TODO решить с помощью list comprehension и распечатать его

dict_one = [{'bin':bin(i), 'dec':(i), 'hex':hex(i), 'oct':oct(i)} for i in range(16)]
pprint(dict_one)

import re

def replace_digit(text, to='0'):
    return re.sub("\d", to, text)

def replace_alphabet(text, to='a'):
    return re.sub("[a-Z]", to, text)
import os
import re

def load_words(filename):
    with open(filename, encoding='latin-1') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words

def findInDict(words, hash):
    # regex match!
    vowel = '[aeiou]*'
    regex = '^' + ''.join([vowel + letter for letter in hash]) + vowel + '$'
    pattern = re.compile(regex)

    for word in words:
        if pattern.match(word):
            print(word)

def findEnglish(hash):
    english_words = load_words('words.txt')
    findInDict(english_words, hash)

def findInAllDictionaries(hash):
    for filename in os.listdir('.'):
        if filename.endswith(".txt"): 
            dict_words = load_words(filename)
            findInDict(dict_words, hash)
        else:
            continue
    

if __name__ == '__main__':
    findEnglish('ccpt')

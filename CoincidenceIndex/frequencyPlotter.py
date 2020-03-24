#!/usr/bin/python3
import string
import matplotlib.pyplot as plt
from sampleData import text1, formatText

'''
Finds the letter frequency in the given piece of 
Formats text using formatText() method
'''
def findLetterFrequency(text: str):
    frequencyList = 26 * [0]
    text = formatText(text)
    baseAsciiValue = 65
    for letter in text:
        frequencyList[ord(letter) - baseAsciiValue] += 1
    
    return frequencyList

'''
Plots frequency of letters to 





'''
def frequencyPlotter(text: str):
    baseAsciiValue = 65
    # frequency = list(zip(findLetterFrequency(text), list(string.ascii_uppercase)))
    # print(frequency)
    fig = plt.bar(list(string.ascii_uppercase), findLetterFrequency(text))
    
    plt.title('Letter Frequency of each letter of the alphabet')
    plt.ylabel('Letter frequency')
    plt.xlabel('letters')

    # langs = ['C', 'C++', 'Java', 'Python', 'PHP']
    # students = [23,17,35,29,12]
    plt.show()

frequencyPlotter(text1)
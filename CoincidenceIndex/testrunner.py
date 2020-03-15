#!/usr/bin/python3
from coincidenceIndex import checkCoincidenceIndex, formatText
from sampleData import text1, text2

print(checkCoincidenceIndex(formatText(text1), 1.73))
print(checkCoincidenceIndex(formatText(text2), 1.73))
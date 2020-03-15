#!/usr/bin/python3

'''
Finds the coincidence index for the piece of text
Does not format the text so make sure to pass in a formatted one
'''
def findCoincidenceIndex(text: str, shift: int):
    shiftedText = text[:-(shift)]
    text = text[shift:]
    shiftedLen = len(shiftedText)
    similarCount = 0
    for i in range(shiftedLen):
        if text[i] == shiftedText[i]:
            similarCount += 1 
    
    coincidenceIndex = similarCount/shiftedLen * 26
    return coincidenceIndex

'''
Check all coincidence indices.
Returns the max of the coincidence indices, and the array of indices
Does not format the input
'''
def findBestCoincidenceIndex(text: str):
    textLen = len(text)
    indices = []
    mx = 0
    shift = -1
    for i in range(1, textLen - 2):
        index = findCoincidenceIndex(text, i)
        if (index > mx):
            mx = index
            shift = i
        indices.append(index)

    return {'bestIndex': mx, 'bestShift': shift, 'indices': indices}

'''
Checks if the coincidenceIndex of a piece of text is similar i.e within the error margin to given coincidence index. If yes, then the shift and the index is returned, otherwise false
'''
def checkCoincidenceIndex(text: str, ci: float, errorMargin: float = 0.01):
    textLen = len(text)
    indices = []
    bestIndex = 0
    shift = -1
    for i in range(1, textLen - 2):
        index = findCoincidenceIndex(text, i)
        # print (index - ci)
        diff = abs(index - ci)
        if (diff < errorMargin):
            if diff < abs(bestIndex - ci):
                bestIndex = index
                shift = i
            indices.append((bestIndex, i))

    return {'bestIndex': bestIndex, 'bestShift': shift, 'indices': indices} if shift != -1 else False


'''
Format text before finding coincidence index
Removes: spaces, tabs, newlines, crlf
Converts text to uppercase
'''
def formatText(text: str):
    text = text.replace(' ', '')
    text = text.replace('\t', '')
    text = text.replace('\r\n', '')
    text = text.replace('\n', '')
    text = text.upper()
    return text

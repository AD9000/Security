#!/usr/bin/python3

text1 = 'LRFKQ YUQFJ KXYQV NRTYS FRZRM ZLYGF'\
'VEULQ FPDBH LQDQR RCRWD NXEUO QQEKL'\
'AITGD PHCSP IJTHB SFYFV LADZP BFUDK'\
'KLRWQ AOZMI XRPIF EFFEC LHBVF UKBYE'\
'QFQOJ WTWOS ILEEZ TXWJL KNGBQ QMBXQ'\
'CQPTK HHQRQ DWFCA YSSYO QCJOM WUFBD'\
'FXUDZ HIFTA KCZVH SYBLO ETSWC RFHPX'\
'PRBSS HSJXD FILEB XWBCT OAYAX ZFBJB'\
'KRXIR IMQPZ WMSHL PJHTA ZHBUX HWADL'\
'PTOYE ZIWKM GSOVQ ZGDIX RPDDZ PLCRW'\
'NQWQE CYJYI BYJYK MJFQW LTVZK QTPVO'\
'LPHCK CYUFD QMLGL IMKLF ZKTGY GDTTN'\
'HCVPF DFBRP ZLKVS HWYWS HTDGM BQBKK'\
'XCVGU MONMW VYTBY TNUQH MFJAQ TGNGC'\
'WKUZY AMNER PHFMW EVHWL EZOHY EEHBR'

text2 = 'NUFTD WHFTW HFQUU VZXCX FFINA XMHMT'\
'MHFHC XFFTZ AHXMT YUCXM HHAXN TFXNJ'\
'HZTNX VATCU ZUNAH ATNTZ XDFTZ MUTAU'\
'ZAXMH LXCNT NXACX WXMUN DVTNH OCTDH'\
'YUCFQ UTRZH CXFFT ZATCX FFQHV MUHZD'\
'UVZXD ATCHX YHFFT NXTRC XZMUF QUDHX'\
'ZXCCX ZAUHJ XCHXD YUAAH MUNFT DWTVD'\
'XZMTV ZNHZR VXRRH TXJTN AUDFH UZAHL'\
'HFTWX XZFQU UDTYC XAAVA ATXFX CXAAU'\
'CUFTW HFTTR ZHCXF FIZAT QXVZH ZACTM'\
'VGHTZ ULTZM XWUZA XNUXW HTXJJ HDTFQ'\
'UDYHU RXXRC XZMHN HZUUM TJUDX CXWOH'\
'UZAXA XNXZX CCXGH TZUDY UDDTU JTNUZ'\
'AHUCH DTZTM XAHDF HUZAH LHFHF QUMXZ'\
'ZTVZH MUXMU NNXCR TWUZA TFVHR HCUCX'

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
'''
def formatText(text: str):
    text = text.replace(' ', '')
    text = text.replace('\t', '')
    text = text.replace('\r\n', '')
    text = text.replace('\n', '')
    return text


print(checkCoincidenceIndex(formatText(text1), 1.73))
print(checkCoincidenceIndex(formatText(text2), 1.73))
import re

# SeqCal module

def countBases(seq, base): # got bugs
    return seq.count(base.upper())

def gcContent(seq): # got bugs
    return (countBases(seq, 'G') + countBases(seq, 'C')) / len(seq)

def atContent(seq): # got bugs
    # A+T/(A+T+G+C)
    # use countBase function to count bases
    return (countBases(seq, 'A') + countBases(seq, 'T')) / len(seq)

def countBasesDict(seq): # got bugs
    basesM = {}
    for base in seq:
        if base in basesM:
            basesM[base] += 1
        else:
            basesM[base] = 1
    return basesM
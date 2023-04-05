
import string 
import sys

"""
Comments for technical understanding (starting at "for line in file"):
for each line in the file.
limit range to len(line)-1 because index+1 will be requested.
if the current and next characters are letters.
pair is the lower-case concatenation of the 2 letters.
if pair is already in freqDict, increase frequency.
otherwise make new dictionary entry with value 1.
"""

def countPairs(fileName): 
    file = open(fileName)
    freqDict = {}
    for line in file: 
        for index in range(len(line)-1): 
            if line[index].isalpha() and line[index+1].isalpha():
                pair = line[index].lower() + line[index+1].lower() 
                if pair in freqDict: 
                    freqDict[pair] += 1
                else: 
                    freqDict[pair] = 1
    return freqDict

"""
Comments for technical understanding:
sort freqDict alphabetically by key first, note that sorted() returns a list of tuples.
now sort that list of tuples by value (the second item in the tuple, lambda index 1).
sorted() is a stable sort, so the alphabetic order will be maintained.
reverse = True indicates descending order.
fullySortedList now holds ties in alphabetical order, and all values are descending.

if fewer than 5 pairs, return fullySortedList immediately.
otherwise we have 2 things to track: the index where we delete the remainder of the 
list, and the previous frequency.
index is the index we are at in fullySortedList, x is the pair, y is the frequency.
if this is a new frequency, see if we have process at least 5 items. 
if we have, return fullySortedList immediately.
otherwise, set prevFreq.
if we have reached the end of the list, return fullySortedList.
"""

def getTopFivePairs(freqDict):
    returnList = []
    sortedAlphaList = sorted(freqDict.items(), key = lambda x:x[0])
    fullySortedList = sorted(sortedAlphaList, key = lambda x:x[1], reverse = True)
    
    if len(fullySortedList) < 5:
        return fullySortedList
    else: 
        prevFreq = 0 
        for index, (x, y) in enumerate(fullySortedList): 
            if y != prevFreq:
                if (index >= 4): 
                    return fullySortedList[0:index]
                prevFreq = y
            if index == len(fullySortedList)-1:
                return fullySortedList           

"""
Comments for technical understanding:
create dictionary of lowercase alphabet with all values initialized to 0.
search through all the pairs, is the first character in the pair is the given 
character, then the second character 'follows' it. 
so, put the freq od the pair into the second character's item in the dictionary.
"""

def createFollowsDict(freqDict, c):
    #creates dictionary of lowercase alphabet and all values 0
    alphaDict = dict.fromkeys(string.ascii_lowercase, 0)
    for x, y in freqDict.items():
        if x[0] == c:
            alphaDict[x[1]] += y
    return alphaDict

# DRIVER
pairs = countPairs(sys.argv[1])
print(len(pairs)) 
print(sum(pairs.values()))
print(getTopFivePairs(pairs))
for x in "aeiou":
    print(x)
    alphaDict = createFollowsDict(pairs, x)
    freq = []
    alphaDict = {freq.append(y) for (x, y) in alphaDict.items()}
    print(freq)
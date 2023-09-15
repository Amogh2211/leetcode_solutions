########### INPUT ###############

import sys

with open("input.txt", "r") as file:
	data = file.readlines()
	word = []
	for line in data:
		word.append(line.replace('\n',''))


sys.stdout= open('output.txt', 'w')
s = word[0]
t = word[1]
#################################

#           Solution

#################################

def validanagram(s,t):
    # Check for frequency of each? 
    freqS, freqT = {}, {}
	
    for i in range(len(word[0])):
        freqS[s[i]] = 1 + freqS.get(s[i], 0)
        freqT[t[i]] = 1 + freqT.get(t[i], 0)
    return freqS == freqT

print(validanagram(s,t))
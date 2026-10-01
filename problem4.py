"""
Problem 4:
given a non empty string like"code" return a tring like "CCoCodCode"
string_splosion('Code') -> CCoCodCode
string_splosion('abc') ->aababc
string_splosion('ab') ->: 'aab'

"""

def splosion(s: str) -> str:
    splosion = ''
    for i in range (1, len(s)+1):
        splosion += s[0:i]
        #for j in range(0,i)
            #splosion +=s[j]
    return splosion
print(splosion('Code'))
print(splosion('abc'))
print(splosion('ab'))
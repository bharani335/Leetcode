from sys import stdin
from json import loads



def lengthOfLastWord(s: str) -> int:
    return len(s.split()[-1])

f = open('user.out', 'w')
for s in map(loads, stdin):
    print(lengthOfLastWord(s), file=f)
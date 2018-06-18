from collections import Counter

def checkMagazine(magazine, note):
    if (Counter(note) - Counter(magazine)) == {}:
        print('Yes')
    else:
        print('No')

magazine = input().rstrip().split()
note = input().rstrip().split()
checkMagazine(magazine, note)

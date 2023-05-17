import pprint, collections

game = {'topL': ' ', 'topM': 'X', 'topR': ' ', 'midL': 'X','midM': ' ', 'midR': 'X', 'lowL': 'X', 'lowM': ' ', 'lowR': ' '}


winCheck1 = {'topL': 0, 'topM': 0, 'topR': 0}
winCheck2 = {'midL': 0, 'midM': 0, 'midR': 0}
winCheck3 = {'lowL': 0, 'lowM': 0, 'lowR': 0}
winCheck4 = {'topL': 0, 'midL': 0, 'lowL': 0}
winCheck5 = {'topM': 0, 'midM': 0, 'lowM': 0}
winCheck6 = {'topR': 0, 'midR': 0, 'lowR': 0}
winCheck7 = {'topL': 0, 'midM': 0, 'lowR': 0}
winCheck8 = {'lowL': 0, 'midM': 0, 'topR': 0}

winChecker = [winCheck1, winCheck2, winCheck3, winCheck4, winCheck5, winCheck6, winCheck7, winCheck8]


for winCheck in winChecker:
    for key in winCheck.keys():
        if game[key] == 'X':
            winCheck[key] = 1
        else: 
            winCheck[key] = 0

oppBestMoveList = {}

for winCheck in winChecker:
    if sum(winCheck.values()) == 2:
         for key, value in winCheck.items():
            if value == 0:
                print(key)
                oppBestMoveList.setdefault(key,0)
                oppBestMoveList[key] = oppBestMoveList[key] + 1
               
    else: continue
print(pprint.pformat(oppBestMoveList))

print(pprint.pformat(winChecker))
import sys

N = int(sys.stdin.readline())

lst = []

for _ in range(N):
    height, weight = list(map(int, sys.stdin.readline().split()))
    lst.append({'height': height, 'weight': weight, 'rank': 1})

for i in range(N):
    for j in range(N):
        if( (lst[i]['height'] < lst[j]['height']) and (lst[i]['weight'] < lst[j]['weight']) ):
            lst[i]['rank'] += 1

for person in lst:
    print(person['rank'], end=' ')

import sys
from itertools import combinations

read = sys.stdin.readline

N = int(read())
member = range(1, N+1)

board = [list(map(int, read().split())) for _ in range(N)]

minn = float('inf')

# N//2 명씩 나누기 => N C (N//2)

for combi in combinations(member, N//2):
    teamA = set(combi)
    teamB = set(member) - teamA
        
    sumA = 0
    sumB = 0
    
    for i,j in combinations(teamA,2):
        sumA += board[i-1][j-1] + board[j-1][i-1]
    
    for m,n in combinations(teamB,2):
        sumB += board[m-1][n-1] + board[n-1][m-1]
        
    minn = min(minn, abs(sumA-sumB))
    
print(minn)
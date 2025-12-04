# 시간초과

import sys
read = sys.stdin.readline

K,L = map(int, read().split())
nums = []
for _ in range(L):
    nums.append(read().rstrip())

waitlist = []

for num in nums:
    if num not in waitlist:
        waitlist.append(num)
    else:
        # waitlist 에서 num 의 인덱스 찾기
        idx = waitlist.index(num)

        # 뒤에 있는 것들 한 칸씩 당기기
        waitlist = waitlist[0:idx] + waitlist[idx+1:] 

        # 맨 뒤에 append
        waitlist.append(num)

for w in waitlist[:K]:
    print(w)




    

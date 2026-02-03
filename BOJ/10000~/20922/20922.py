import sys
from collections import deque

sys.stdin = open("in.txt", "r")

read = sys.stdin.readline

def solution():
    n, k = map(int, read().split()) # n <= 200,000
    nums = list(map(int, read().split()))
    deq = deque()

    num_dic = dict()

    res = 0

    for num in nums:
        
        if num not in num_dic:
            num_dic[num] = 1
        else:
            num_dic[num] += 1


        deq.append(num) # deq 에 추가
        # print(f"\n before : {num=}, {num_dic=}, {deq=}, {res=}\n")

        if num_dic[num] > k: # 새로운 숫자가 최대빈도수 초과했다면
            while num_dic[num] > k:
                pop_num = deq.popleft() # 맨 왼쪽 수 제거
                num_dic[pop_num] -= 1 # 제거한 수의 횟수 차감

        res = max(res, len(deq))

        # print(f"{num=}, {num_dic=}, {deq=}, {res=}\n")
        
    print(res)



if __name__ == "__main__":
    solution()
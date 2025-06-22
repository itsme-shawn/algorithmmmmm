import sys

n = int(input())
lst = []
for _ in range(n):
    lst.append(int(sys.stdin.readline()))
total = sum(lst)
avg = total / n


print(round(avg))

# print(lst.sort()) # 이건 None 을 리턴함
lst.sort()

print(lst[n // 2])

# 최빈값 계산
freq = dict()
for i in range(n):
    if lst[i] not in freq:
        freq[lst[i]] = 0
    freq[lst[i]] += 1

# 최빈값 하나인지 여러 개인지 체크
freqValLst = list(freq.values())
freqMax = max(freqValLst)
if freqValLst.count(freqMax) == 1:
    for key, value in freq.items():
        if value == freqMax:
            print(key)
else:
    cnt = 0
    for key, value in freq.items():
        if value == freqMax:
            cnt += 1
        if cnt == 2:
            print(key)
            break  # 이 break 안써줘서 계속 출력초과떴음


# 범위(최댓값과 최솟값 차이) 구하기
print(max(lst) - min(lst))

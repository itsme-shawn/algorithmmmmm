import sys
read = sys.stdin.readline

K,L = map(int, read().split())

last_click = dict() # {"sid" : 마지막인덱스}

for i in range(L):
    sid = read().rstrip()
    last_click[sid] = i

# bucket[i] : value 가 i 인 last_click 의 key 값
bucket = [None] * L # last_click 을 정렬 안 하기 위해서 dict 의 k,v 를 뒤집은 배열을 만드는 것

for sid,idx in last_click.items():
    bucket[idx] = sid

i = 0
for sid in bucket: # bucket 순서대로 순회
    if sid is None:
        continue
    print(sid)
    i += 1
    if i == K:
        break


'''
마지막에 등장한 인덱스 기준으로 중복 제거 + 순서유지
정렬을 하지 않기 위해서 bucket 배열 사용
'''
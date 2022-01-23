import sys

word = sys.stdin.readline().rstrip().upper()

w_set = list(set(word))  # 중복제거
w_cnt = []  # w_set 의 개수를 담을 리스트

for ch in w_set:
    w_cnt.append(word.count(ch))  # 개수 저장

if w_cnt.count(max(w_cnt)) > 1:  # 최댓값 개수가 여러개 일 때
    print("?")
else:
    max_idx = w_cnt.index(max(w_cnt))  # w_cnt 에서 최댓값의 인덱스를 찾음
    print(w_set[max_idx])

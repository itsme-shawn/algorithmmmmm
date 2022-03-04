res = [0] * 10001
for num in range(1, 10001):
    temp = num + sum(list(map(int, list(str(num)))))
    res[temp] = 1
for i in range(1, 10001):
    if res[i] == 0:  # 생성자가 없는 경우
        print(i)

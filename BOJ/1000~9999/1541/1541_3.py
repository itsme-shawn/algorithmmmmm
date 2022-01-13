exp = input().split("-")
ans = 0
for i in exp[0].split("+"):  # 첫 번째 인덱스는 다 더해준다
    ans += int(i)

for i in exp[1:]:
    for j in i.split("+"):  # 차례대로 모두 다 빼줌
        ans -= int(j)

print(ans)

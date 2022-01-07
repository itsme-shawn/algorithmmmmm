import sys

string = sys.stdin.readline()

cnt = 0
check = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for item in check:
    # string 에 check item 이 있는지 확인
    if string.count(item):
        # 개수만큼 더해주기
        cnt += string.count(item)
        # 제거
        string = string.replace(item, ",").strip()

        # 단순히 제거만 하면 양 옆의 문자가 합쳐져서 크로아티아 알파벳이 될 수 있으므로 쉼표추가


# 쉼표제거
string = string.replace(",", "").strip()
# 나머지 더해주기
cnt += len(string)

print(cnt)

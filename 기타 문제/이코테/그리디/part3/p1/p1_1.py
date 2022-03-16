import sys

sys.stdin = open("in.txt", "rt")
read = sys.stdin.readline

n = int(read())
nums = list(map(int, read().split()))

nums.sort()
cnt = 0
i, j = 0, 0  # 투포인터 ( i: 시작포인터, j : 끝포인터)
flag = 0
length = len(nums)

# i,j 투 포인터 => 둘 다 length 보다 작을동안만 while loop 반복
while j < length and i < length:

    # 이전 루프에서 flag 가 0 일때만 j 포인터 다시 설정
    if i + (nums[i] - 1) < length and flag == 0:
        j = i + (nums[i] - 1)

    if nums[j] == j - i + 1:
        flag = 0  # flag 가 0 : 현재 loop에서 그룹완성한 상태. i,j 다시 세팅
        cnt += 1  # 그룹개수 증가
        i = j + 1  # i 값 새롭게 세팅
    else:
        flag = 1  # flag 1 : 그룹 완성 못해서 i 값 유지, j 값만 1 증가
        j += 1

print(cnt)

import sys

read = sys.stdin.readline

n, k = map(int, read().split())

nums = list(map(int, read().split()))

psums = [0] * (n + 1)

psum_cnt = {}

ans = 0

# 누적합 생성
for i in range(n):
    psums[i + 1] = psums[i] + nums[i]

# k = psum[j+1] - psum[i]
# 누적합 배열을 순회하면서 psum - k 가 psum_cnt 에 있는지 검사하고
# 있으면 (psum-k) 의 개수만큼 더해준다
# 그 후 psum_cnt 의 psum 값을 1 증가시킨다 (개수 1 증가)
for psum in psums:
    if psum - k in psum_cnt:
        ans += psum_cnt[psum - k]

    psum_cnt[psum] = psum_cnt.get(psum, 0) + 1

print(ans)

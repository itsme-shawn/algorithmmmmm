N = int(input())
A = [0] * N
B = [0] * N

for i in range(N):
    A[i], B[i] = map(int, input().split())

for i in range(N):
    print(f"Case #{i+1}: {A[i]+B[i]}")

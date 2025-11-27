import sys

# sys.stdin = open("in.txt", "r")
read = sys.stdin.readline

def add(S:set, x):
    if x not in S:
        S.add(x)

def remove(S:set, x):
    if x in S:
        S.remove(x)

def check(S:set, x):
    if x in S:
        return 1
    else:
        return 0
    
def toggle(S:set, x):
    if x in S:
        S.remove(x)
    else:
        S.add(x)

def _all(S:set):
    S.clear()
    S.update(range(1,21))
    # return set(range(1,21)) # 이 방식은 비효율

def empty(S:set):
    S.clear()
    # S = set() : 비효율
    # 주의) 이렇게 대입연산을 하면 새로운 지역변수 S 에 할당을 하는 것이므로 인자 S 는 변하지않는다


def solution():
    M = int(read())
    S = set()
    for _ in range(M):
        user_input = read().split()

        cmd = user_input[0]

        if len(user_input) == 2:
            x = int(user_input[1])

        if cmd == "add":
            add(S,x)
            # print(f"{cmd=}, {x=}, {S=}")
        elif cmd == "check":
            # print(f"{cmd=}, {x=}, {S=}")
            print(check(S,x))
        elif cmd == "remove":
            remove(S,x)
            # print(f"{cmd=}, {x=}, {S=}")
        elif cmd == "toggle":
            toggle(S,x)
            # print(f"{cmd=}, {x=}, {S=}")
        elif cmd == "all":
            _all(S)
            # print(f"{cmd=}, {x=}, {S=}")
        elif cmd == "empty":
            empty(S)
            # print(f"{cmd=}, {x=}, {S=}")
    
if __name__ == "__main__":
    solution()
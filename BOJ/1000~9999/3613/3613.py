import sys
read = sys.stdin.readline

def solution():
    s = read().rstrip()

    # 1. 기본 에러 체크
    # 비어 있으면 안 됨
    # 맨 앞/뒤에 '_' 오면 안 됨
    # 첫 글자가 대문자면 안 됨
    # 연속 '__" 이면 안 됨
    if not s or s[0] == "_" or s[-1] == "_" or s[0].isupper() or '__' in s:
        print("Error!")
        return

    has_underscore = '_' in s # c++
    has_upper = any(ch.isupper() for ch in s) # java

    # 2. c++, java 규칙 동시에 섞인 경우 는 error
    if has_underscore and has_upper:
        print("Error!")
        return

    # 3. c++ -> java 형식
    if has_underscore:
        parts = s.split('_')
        
        # parts 중에 빈 문자열이 있으면 Error
        if any(len(p) == 0 for p in parts):
            print("Error!")
            return

        res = parts[0]
        for word in parts[1:]:
            res += word[0].upper() + word[1:]
        print(res)
        return

    # 4. java -> c++ 형식
    if has_upper:
        res = []
        for ch in s:
            if ch.isupper():
                res.append('_')
                res.append(ch.lower())
            else:
                res.append(ch)
        print("".join(res))
        return
    
    # 5. 둘 다 가능한 평범한 문자 (ex abc => 그대로 abc 출력)
    print(s)

if __name__ == "__main__":
    solution()


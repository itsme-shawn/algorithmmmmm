import sys
read = sys.stdin.readline

def solution():
    s = read().rstrip()

    is_tag = False
    common_word = ""
    
    res = ""

    for ch in s:
        if ch == '<':
            # 일반단어 뒤집어서 res 에 저장
            res += "".join(map(str,reversed(common_word)))
            common_word = ""

            # tag flag True 처리하고 res에 '<' 추가
            is_tag = True
            res += '<'
        elif ch == ' ':
            # 일반단어 뒤집어서 res 에 저장
            res += "".join(map(str,reversed(common_word)))
            common_word = ""

            res += " "
        elif is_tag:
            if ch == '>':
                is_tag = False
            res += ch
        else: # 일반 단어
            common_word += ch
    
    # 마지막에 일반단어 추가
    res += "".join(map(str,reversed(common_word)))

    print(res)
        

if __name__ == "__main__":
    solution()
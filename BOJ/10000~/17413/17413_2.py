import sys
read = sys.stdin.readline

def solution():
    s = read().rstrip()

    is_tag = False

    word_buf = [] # 현재 단어를 모아두는 임시버퍼
    res = [] # 결과 저장할 리스트

    # 단어 뒤집어서 추가
    def flush_word():
        nonlocal word_buf, res
        if word_buf:
            res.extend(word_buf[::-1])
            # res.extend(reversed(word_buf) 와 동일
            
            word_buf = []

    for ch in s:
        if ch == '<':
            # 단어와 태그의 경계 : 지금까지의 단어 뒤집어서 추가
            flush_word()

            # tag flag True 처리하고 res 에 '<' 추가
            is_tag = True
            res.append('<')
        elif ch == ' ':
            # 일반단어 뒤집어서 res 에 저장
            flush_word()
            res.append(" ") # 공백 추가
        elif is_tag: # 태그 안 문자
            res.append(ch)
            if ch == '>':
                is_tag = False
        else: # 태그 밖 일반 문자
            word_buf.append(ch)
    
    # 마지막에 일반단어 추가
    flush_word()

    print("".join(res))
        

if __name__ == "__main__":
    solution()
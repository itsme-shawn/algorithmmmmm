import sys
read = sys.stdin.readline

n,m = map(int, read().split())

'''
M 글자수 이상인 단어만
자주 나오는 단어일수록 앞에 배치한다.
해당 단어의 길이가 길수록 앞에 배치한다.
알파벳 사전 순으로 앞에 있는 단어일수록 앞에 배치한다
'''

words = dict()

for _ in range(n):
    word = read().rstrip()
    if len(word) >= m:
        if word not in words:
            words[word] = 1
        else:
            words[word] += 1

sorted_words = sorted(list(words.items()), key = lambda x : (-x[1], -len(x[0]), x[0]))

for word in sorted_words:
    print(word[0])


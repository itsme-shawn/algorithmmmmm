import re
import sys

read = sys.stdin.readline

numbers = list(map(str, range(0, 10)))


def solution(accounts):
    account_types = {}

    for account in accounts:
        flag = 1

        # 규칙 1,2,3
        if flag:
            num_cnt = 0
            dash_cnt = 0
            for ch in account:
                if ch in numbers:
                    num_cnt += 1
                elif ch == "-":
                    dash_cnt += 1
                else:
                    flag = 0
                    break
            if 11 <= num_cnt <= 14 and 0 <= dash_cnt <= 3:
                pass
            else:
                flag = 0

        # 규칙 4-2
        if flag:
            first = account[0]
            last = account[-1]
            if first != "-" and last != "-":
                pass
            else:
                flag = 0

            before = first
            for cur in account:
                if before == "-" and cur == "-":
                    flag = 0
                    break
                before = cur

        # 규칙 4-1
        if flag:
            txt = re.sub("[0-9]", "X", account)
            if txt not in account_types:
                account_types[txt] = 1
            else:
                account_types[txt] += 1

    answer = sorted(list(account_types.values()), reverse=True)

    return answer

# https://school.programmers.co.kr/learn/courses/30/lessons/42891
# 무지의 먹방 라이브


def solution(food_times, k):
    answer = 0
    length = len(food_times)
    sec = 0
    flag = 0

    while True:
        for i in range(length):
            if max(food_times) == 0:  # 먹방을 할 수 없는 경우에는 while문 break
                answer = -1
                flag = 1
                break
            elif food_times[i] > 0:  # 먹방 가능한 경우
                if sec == k:  # 탈출
                    answer = i + 1
                    flag = 1
                    break
                else:  # 먹방하고 시간증가
                    food_times[i] -= 1
                    sec += 1
        if flag == 1:
            break

    return answer


# 정확성 테스트는 다 통과지만
# 효율성 테스트에서 다 시간초과

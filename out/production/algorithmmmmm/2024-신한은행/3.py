from collections import defaultdict, deque


def solution(vote):
    n = len(vote)
    results = [0] * (n + 1)

    # 기본 투표 결과를 반영하여 초기 확정 시점 찾기
    vote_count = defaultdict(int)
    max_votes = 0
    leading = deque()

    for i in range(n):
        vote_count[vote[i]] += 1
        if vote_count[vote[i]] > max_votes:
            max_votes = vote_count[vote[i]]
            leading = deque([vote[i]])
        elif vote_count[vote[i]] == max_votes:
            leading.append(vote[i])

        if len(leading) == 1:
            results[0] = i + 1

    # k개의 표를 수정할 때마다 확정 시점을 구하기
    for k in range(1, n + 1):
        temp_vote_count = vote_count.copy()
        temp_leading = leading.copy()
        temp_max_votes = max_votes

        for i in range(n):
            if (
                vote_count[vote[i]] == temp_max_votes
                and len(temp_leading) == 1
                and temp_leading[0] == vote[i]
            ):
                temp_vote_count[vote[i]] -= 1
                if temp_vote_count[vote[i]] == temp_max_votes - 1:
                    temp_max_votes -= 1
                    temp_leading = deque(
                        [
                            key
                            for key in temp_vote_count
                            if temp_vote_count[key] == temp_max_votes
                        ]
                    )
                elif temp_vote_count[vote[i]] < temp_max_votes:
                    temp_leading = deque(
                        [
                            key
                            for key in temp_vote_count
                            if temp_vote_count[key] == temp_max_votes
                        ]
                    )

            for r in range(1, n + 1):
                if r != vote[i]:
                    temp_vote_count[r] += 1
                    if temp_vote_count[r] > temp_max_votes:
                        temp_max_votes = temp_vote_count[r]
                        temp_leading = deque([r])
                    elif temp_vote_count[r] == temp_max_votes:
                        temp_leading.append(r)
                    temp_vote_count[r] -= 1

            if len(temp_leading) == 1:
                results[k] = i + 1
                break

    return results


# 예제 테스트
print(
    solution([1, 1, 1, 1, 1, 3, 2, 2, 1, 2])
)  # [7, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10]
print(solution([5, 5, 5, 5, 5, 8, 7, 7, 5]))  # [5, 9, 9, 9, 9, 9, 9, 9, 9, 9]

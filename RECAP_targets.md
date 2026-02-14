# 미복기 추천 문제 (코드만 있음 → 복기 대상)
레포에 코드만 있고 md 복기가 없는 문제 중, 코테 대비로 다시 풀어볼 만한 실버 상위~골드 문제들입니다. 링크는 백준 문제 페이지를 가리킵니다.

## DP
| 플랫폼 | 티어 | 문제번호 및 문제명(링크) | 주요 도구/아이디어 |
| --- | --- | --- | --- |
| BOJ | G4 | [11053. 가장 긴 증가하는 부분 수열](https://www.acmicpc.net/problem/11053) | LIS, `dp` 혹은 이분 탐색 패턴 |
| BOJ | S3 | [11726. 2×n 타일링](https://www.acmicpc.net/problem/11726) | 피보나치형 DP, 모듈러 주의 |
| BOJ | S3 | [14501. 퇴사](https://www.acmicpc.net/problem/14501) | 역방향 일정 DP, 최대 수익 |

## 그래프/DFS/BFS/최단거리
| 플랫폼 | 티어 | 문제번호 및 문제명(링크) | 주요 도구/아이디어 |
| --- | --- | --- | --- |
| BOJ | S2 | [11724. 연결 요소의 개수](https://www.acmicpc.net/problem/11724) | DFS/BFS로 컴포넌트 카운트 |
| BOJ | S2 | [11725. 트리의 부모 찾기](https://www.acmicpc.net/problem/11725) | BFS/DFS로 부모 저장 |
| BOJ | G3 | [11779. 최소비용 구하기 2](https://www.acmicpc.net/problem/11779) | 다익스트라 + 경로 복원 |
| BOJ | G3 | [16236. 아기 상어](https://www.acmicpc.net/problem/16236) | BFS 탐색 + 우선순위 선택(거리/행/열) |

## 스택/모노톤/그리디
| 플랫폼 | 티어 | 문제번호 및 문제명(링크) | 주요 도구/아이디어 |
| --- | --- | --- | --- |
| BOJ | G4 | [17298. 오큰수](https://www.acmicpc.net/problem/17298) | 모노톤 스택으로 다음 큰 값 |
| BOJ | G5 | [14719. 빗물](https://www.acmicpc.net/problem/14719) | 좌/우 최대 높이 또는 스택/투포인터로 물량 계산 |

## 브루트포스/백트래킹/시뮬레이션
| 플랫폼 | 티어 | 문제번호 및 문제명(링크) | 주요 도구/아이디어 |
| --- | --- | --- | --- |
| BOJ | G4 | [14500. 테트로미노](https://www.acmicpc.net/problem/14500) | 브루트포스 + 예외(T자) 처리 |
| BOJ | G4 | [14502. 연구소](https://www.acmicpc.net/problem/14502) | 조합(벽 3개) + BFS로 확산 시뮬 |
| BOJ | G4 | [15683. 감시](https://www.acmicpc.net/problem/15683) | CCTV 방향 완전탐색, 시야 시뮬레이션 |
| BOJ | S1 | [14888. 연산자 끼워넣기](https://www.acmicpc.net/problem/14888) | 연산자 순열 백트래킹 |
| BOJ | S2 | [14889. 스타트와 링크](https://www.acmicpc.net/problem/14889) | 조합 분할 + 시너지 합계 |

## 정렬/그리디/자료구조
| 플랫폼 | 티어 | 문제번호 및 문제명(링크) | 주요 도구/아이디어 |
| --- | --- | --- | --- |
| BOJ | S3 | [13305. 주유소](https://www.acmicpc.net/problem/13305) | 그리디: 최소 가격 유지하며 이동 |
| BOJ | S3 | [13458. 시험 감독](https://www.acmicpc.net/problem/13458) | 몫/나머지 기반 감독 수 계산 |

## 구현/시뮬레이션 추가
| 플랫폼 | 티어 | 문제번호 및 문제명(링크) | 주요 도구/아이디어 |
| --- | --- | --- | --- |
| BOJ | G5 | [20055. 컨베이어 벨트 위의 로봇](https://www.acmicpc.net/problem/20055) | 회전·내구도·로봇 이동 시뮬레이션 |
| BOJ | G4 | [14503. 로봇 청소기](https://www.acmicpc.net/problem/14503) | 방향 전환 규칙 시뮬레이션, 후진 처리 |

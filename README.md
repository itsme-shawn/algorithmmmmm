# algorithmmmmm🧐

[![Solved.ac
프로필](http://mazassumnida.wtf/api/v2/generate_badge?boj=soul4927)](https://solved.ac/soul4927)

## 문제 분류 (유형별)

### DP
| 플랫폼 | 티어 | 문제번호 및 문제명(링크) | 주요 도구/아이디어 |
| --- | --- | --- | --- |
| BOJ | G5 | [12865. 평범한 배낭](https://www.acmicpc.net/problem/12865) | 0/1 배낭 DP, 1차원 역순 갱신 |
| BOJ | S1 | [2156. 포도주 시식](https://www.acmicpc.net/problem/2156) | 연속 3잔 불가 조건을 반영한 3상태 DP |
| BOJ | G4 | [14722. 우유 도시](https://www.acmicpc.net/problem/14722) | 격자 DP, DP 값 전이 이후 마신 잔 수의 mod 3로 다음 우유 결정 |

### 그래프/최단거리
| 플랫폼 | 티어 | 문제번호 및 문제명(링크) | 주요 도구/아이디어 |
| --- | --- | --- | --- |
| BOJ | S1 | [14940. 쉬운 최단거리](https://www.acmicpc.net/problem/14940) | 목표 지점 역방향 BFS, 격자 최단거리 |
| BOJ | G4 | [4179. 불!](https://www.acmicpc.net/problem/4179) | 불 다중 시작 BFS + 사람 BFS로 도달 가능 시간 비교 |
| BOJ | G5 | [21278. 호석이 두 마리 치킨](https://www.acmicpc.net/problem/21278) | 플로이드-워셜로 전쌍 최단거리 후 두 지점 조합 최소화 |

### 우선순위 큐/힙
| 플랫폼 | 티어 | 문제번호 및 문제명(링크) | 주요 도구/아이디어 |
| --- | --- | --- | --- |
| BOJ | S1 | [11286. 절댓값 힙](https://www.acmicpc.net/problem/11286) | 최소힙, `(abs(x), x)` 튜플 비교 |
| BOJ | G4 | [2696. 중앙값 구하기](https://www.acmicpc.net/problem/2696) | 두 힙 균형 유지(max-heap/min-heap)로 중앙값 스트리밍 |

### 정렬/자료구조
| 플랫폼 | 티어 | 문제번호 및 문제명(링크) | 주요 도구/아이디어 |
| --- | --- | --- | --- |
| BOJ | S3 | [20920. 영단어 암기는 괴로워](https://www.acmicpc.net/problem/20920) | 다중 키 정렬 (빈도 ↓, 길이 ↓, 사전순 ↑) |
| BOJ | S2 | [18870. 좌표 압축](https://www.acmicpc.net/problem/18870) | 정렬 후 인덱스 매핑으로 좌표 압축 |
| BOJ | S3 | [1431. 시리얼 번호](https://www.acmicpc.net/problem/1431) | 길이 → 숫자합 → 사전순 정렬 |
| BOJ | S3 | [13414. 수강신청](https://www.acmicpc.net/problem/13414) | 해시로 마지막 신청만 유지, 입력 순서 기반 선택 |
| BOJ | S3 | [20291. 파일 정리](https://www.acmicpc.net/problem/20291) | 확장자 빈도 집계 후 사전순 출력 |

### 문자열/파싱
| 플랫폼 | 티어 | 문제번호 및 문제명(링크) | 주요 도구/아이디어 |
| --- | --- | --- | --- |
| BOJ | S3 | [17413. 단어 뒤집기 2](https://www.acmicpc.net/problem/17413) | 상태 전환(태그/바깥) + 스택을 통한 단어 뒤집기 |
| BOJ | S4 | [3613. Java vs C++](https://www.acmicpc.net/problem/3613) | 입력 형식 검증 후 케이스 변환 (camel ↔ snake) |

### 트리/재귀
| 플랫폼 | 티어 | 문제번호 및 문제명(링크) | 주요 도구/아이디어 |
| --- | --- | --- | --- |
| BOJ | S1 | [5639. 이진 검색 트리](https://www.acmicpc.net/problem/5639) | 전위 순회 분할 정복, 후위 순회 재귀 출력 |
| BOJ | S1 | [9934. 완전 이진 트리](https://www.acmicpc.net/problem/9934) | 중위 리스트 중앙 기준 분할, 레벨별 수집 |

### 투 포인터/슬라이딩 윈도우
| 플랫폼 | 티어 | 문제번호 및 문제명(링크) | 주요 도구/아이디어 |
| --- | --- | --- | --- |
| BOJ | S1 | [20922. 겹치는 건 싫어](https://www.acmicpc.net/problem/20922) | 빈도 카운트하며 두 포인터로 최대 구간 길이 |

### 완전탐색/부분집합
| 플랫폼 | 티어 | 문제번호 및 문제명(링크) | 주요 도구/아이디어 |
| --- | --- | --- | --- |
| BOJ | G4 | [19942. 다이어트](https://www.acmicpc.net/problem/19942) | 모든 부분집합 탐색, 영양 조건 만족 시 비용 최소 갱신 |

### 모노톤 스택
| 플랫폼 | 티어 | 문제번호 및 문제명(링크) | 주요 도구/아이디어 |
| --- | --- | --- | --- |
| BOJ | G5 | [2493. 탑](https://www.acmicpc.net/problem/2493) | 높이 내림차순 유지 스택으로 최근 더 높은 탑 찾기 |

### 구현/시뮬레이션
| 플랫폼 | 티어 | 문제번호 및 문제명(링크) | 주요 도구/아이디어 |
| --- | --- | --- | --- |
| BOJ | S2 | [20006. 랭킹전 대기열](https://www.acmicpc.net/problem/20006) | 조건에 맞는 방 선형 탐색 후 삽입, 정렬 출력 |
| BOJ | S1 | [1713. 후보 추천하기](https://www.acmicpc.net/problem/1713) | 추천 수·시간 기준으로 사진틀 교체를 시뮬레이션 |
| BOJ | G5 | [14891. 톱니바퀴](https://www.acmicpc.net/problem/14891) | 회전 전달 방향을 구해 기어 상태를 순차 갱신 |

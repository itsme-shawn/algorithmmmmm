def solution(citations):
    answer = 0
    
    citations.sort(reverse=True)

    for i in range(len(citations)):
        # 인용횟수 : i 번
        # i번 인용된 논문 갯수 : citations[]
        
            
    return answer

# citations = [3, 0, 6, 1, 5]
citations = [1,2,2,2,3,5,6]
print(solution(citations))
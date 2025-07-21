def solution(prices):
    length = len(prices)
    
    stack = []
    res = [0] * length
    
    for i in range(0, length-1):
        cur = prices[i]
        nxt = prices[i+1]
        
        stack.append(i)
        if cur > nxt:
            while stack and prices[stack[-1]] > nxt:
                idx = stack.pop()
                res[idx] = i + 1 - idx
    
    # 나머지
    while stack:
        idx = stack.pop()
        res[idx] = (length - 1) - idx

    return res

prices = [1,2,3,4,2,2,3]
# prices = [1,2,3,2,3]
print(solution(prices))

'''
1               

'''
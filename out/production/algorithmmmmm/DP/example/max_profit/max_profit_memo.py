# memoization 방식 (top-down)
def max_profit_memo(price_list, count, cache):
    # base case
    cache[0] = price_list[0]
    cache[1] = price_list[1]

    # 이미 계산된 값이면 cache 에 저장된 값 리턴
    if count in cache:
        return cache[count]

    # else :
    temp = []

    if( count < len(price_list)):
        temp.append(price_list[count])
        
    for i in range(1, count//2 + 1):
        if( count-i not in cache ):
            cache[count-i] = max_profit_memo(price_list, count-i, cache)
        temp.append( cache[i] + cache[count-i] )
    
    cache[count] = max(temp)

    return cache[count]
    
def max_profit(price_list, count):
    max_profit_cache = {}

    return max_profit_memo(price_list, count, max_profit_cache)


# 테스트
print(max_profit([0, 100, 400, 800, 900, 1000], 5))
print(max_profit([0, 100, 400, 800, 900, 1000], 10))
print(max_profit([0, 100, 400, 800, 900, 1000, 1400, 1600, 2100, 2200], 9))

print(max_profit([0, 200, 600, 900, 1200, 2000], 5))
print(max_profit([0, 300, 600, 700, 1100, 1400], 8))
print(max_profit([0, 100, 200, 400, 600, 900, 1200, 1300, 1500, 1800], 9))

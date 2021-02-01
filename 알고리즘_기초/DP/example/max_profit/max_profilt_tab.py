# Tabulation 방식 (bottom-up)
def max_profit(price_list, count):
    table = [-1] * (count+1)

    table[0] = price_list[0]
    table[1] = price_list[1]

    for i in range(2, count+1):
        temp = []
        if( i < len(price_list)):
            temp.append(price_list[i])
        
        for j in range(1, i//2 + 1):
            temp.append( table[j] + table[i-j])
        
        table[i] = max(temp)
    
    return table[count]


# 테스트
print(max_profit([0, 100, 400, 800, 900, 1000], 5))
print(max_profit([0, 100, 400, 800, 900, 1000], 10))
print(max_profit([0, 100, 400, 800, 900, 1000, 1400, 1600, 2100, 2200], 9))

print(max_profit([0, 200, 600, 900, 1200, 2000], 5))
print(max_profit([0, 300, 600, 700, 1100, 1400], 8))
print(max_profit([0, 100, 200, 400, 600, 900, 1200, 1300, 1500, 1800], 9))

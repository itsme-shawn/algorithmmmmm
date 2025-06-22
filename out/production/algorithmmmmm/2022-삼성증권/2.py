def solution(k, rates):
    money = k

    flag = 0  # 0 : 안 산 상태 , 1 : 현재 산 상태
    buy_price = 0
    win = 0

    for i in range(len(rates) - 1):
        # print("현재금액",money)
        # 사는 상황
        # 현재 돈이 환율보다 많고,
        # 오늘 환율보다 바로 다음 날 환율이 비싸면 삼
        if rates[i + 1] > rates[i] and money >= rates[i] and flag == 0:
            # print("BUY", rates[i])
            buy_price = rates[i]
            money -= buy_price
            flag = 1

        # 파는 상황
        # flag 가 1이고,
        # 오늘환율 > 내일환율 and 오늘환율 > 산 가격 이면 팔아야함
        elif rates[i] > rates[i + 1] and rates[i] > buy_price and flag == 1:
            # print("SELL", rates[i])
            win += rates[i] - buy_price
            money += rates[i]
            flag = 0

    # 마지막 원소처리
    # flag 가 1이고,
    # 오늘 환율 > 산 가격이면 팔아야함
    if flag == 1 and rates[-1] > buy_price:
        # print("SELL", rates[-1])
        win += rates[-1] - buy_price
        money += rates[-1]
        flag = 0

    # print("win",win)
    # print("최종돈",money)

    return money

# 거스름돈을 최소한의 동전 갯수로 거슬러주기
# min_coin_count(value, coin_list) : 거슬러 주기 위해 필요한 최소 동전 개수 리턴
# default_coin_list : 동전 종류


def min_coin_count(value, coin_list):
    coin_list.sort(reverse=True)  # [500, 100, 50, 10]
    count = 0
    for coin in coin_list:
        count += value // coin
        value = value % coin
    return count


default_coin_list = [100, 500, 10, 50]

print(min_coin_count(1440, default_coin_list))
print(min_coin_count(1700, default_coin_list))
print(min_coin_count(23520, default_coin_list))
print(min_coin_count(32590, default_coin_list))

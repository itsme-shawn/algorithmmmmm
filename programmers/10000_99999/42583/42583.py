from collections import deque


def solution(bridge_length, weight, truck_weights):
    time = 0
    truck_wait_q = deque(enumerate(truck_weights))
    print(truck_wait_q)
    # [[truck_num, truck_weigh], ..]

    bridge_q = deque()
    # [[truck_num, truck_weigh, left_second], ...]

    cur_weight = 0

    while True:

        print("===========")

        time += 1
        
        
        print("time", time)

        # 다리큐에서 트럭들 진행시키기 (시간감소)
        if bridge_q:
            print(f"check bridge_q : {bridge_q}")
            for truck_info in bridge_q:
                # truck_info = [truck_num, truck_weigh, left_second]
                print(f"truck_info : {truck_info}")
                if truck_info[2] > 0:
                    truck_info[2] -= 1
                if truck_info[2] == 0:
                    # popleft 대신 1 추가감소
                    truck_info[2] -= 1
                    cur_weight -= truck_info[1]

        print("before cur_weight", cur_weight)
        
        # 대기큐에서 빼서 다리큐에 넣는다
        if truck_wait_q and truck_wait_q[0][1] + cur_weight <= weight:
            add_truck_num, add_truck_weight = truck_wait_q.popleft()

            bridge_q.append([add_truck_num, add_truck_weight, bridge_length])
            cur_weight += add_truck_weight

        print(f"bridge_q : {bridge_q}")
        print("after cur_weight", cur_weight)
        print(f"truck_wait_q : {truck_wait_q}")

        print("===========")

        if not truck_wait_q:

            # 다리에 남아있는 트럭 나머지 시간 진행
            time += bridge_length
            break

    return time


"""
bridge_length	weight	truck_weights	return
2	10	[7,4,5,6]	8
100	100	[10]	101
100	100	[10,10,10,10,10,10,10,10,10,10]	110
"""

bridge_length = 2
weight = 10
truck_weights = [7, 4, 5, 6]

print(solution(bridge_length, weight, truck_weights))

"""
경과 시간	다리를 지난 트럭	다리를 건너는 트럭	대기 트럭
0	[]	[]	[7,4,5,6]
1~2	[]	[7]	[4,5,6]
3	[7]	[4]	[5,6]
4	[7]	[4,5]	[6]
5	[7,4]	[5]	[6]
6~7	[7,4,5]	[6]	[]
8	[7,4,5,6]	[]	[]


"""

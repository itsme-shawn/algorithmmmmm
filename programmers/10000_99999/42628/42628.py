import heapq as hq

def printt(answer, min_heap, max_heap, master, *args):
    return
    print(f"{answer=}, {min_heap=}, {max_heap=}, {master=}", *args)
    

def solution(operations):
    answer = []
    min_heap = []
    max_heap = []
    master = dict() # {id : num}
    id = 0
    printt(answer, min_heap, max_heap, master)
    
    for oper in operations:
        op, num = oper.split()
        printt(answer, min_heap, max_heap, master,1)
        num = int(num)
        if op == "I":
            
            printt(answer, min_heap, max_heap, master,2)
            # min, max heap 에 삽입
            hq.heappush(min_heap, (num,id))
            hq.heappush(max_heap, (-num,id))
            
            # master dict 에도 삽입
            master[id] = num
            
            id += 1
            
        elif op == "D" and master and min_heap and max_heap:
            printt(answer, min_heap, max_heap, master,3)
            if num == -1: # 최솟값 삭제                
                while min_heap:
                    printt(answer, min_heap, max_heap, master,4)
                    _, _id = hq.heappop(min_heap)
                    if _id in master:
                        del master[_id]
                        break
            if num == 1: # 최댓값 삭제                
                while max_heap:
                    printt(answer, min_heap, max_heap, master,5)
                    _, _id = hq.heappop(max_heap)
                    if _id in master:
                        del master[_id]
                        break
                    
        printt(answer, min_heap, max_heap, master,6)
                          
    if not master:
        answer = [0,0]
    else:
        # master 랑 min_heap, max_heap 동기화
        while min_heap:
            val, _id = min_heap[0]
            if _id in master:
                min_val = val
                break
            else:
                hq.heappop(min_heap)
                
        while max_heap:
            val, _id = max_heap[0]
            if _id in master:
                max_val = -val
                break
            else:
                hq.heappop(max_heap)
            
        answer = [max_val, min_val]
            
    return answer


# operations = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
print(solution(operations))
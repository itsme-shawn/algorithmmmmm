def solution(tickets):    
    ans = []
    # 그래프 형태로 변환
    graph = {}
    
    for ticket in tickets:
        start = ticket[0]
        end = ticket[1]
        visited = False
        
        graph[start] = graph.get(start, []) + [[end, visited]]
        
    # 목적지 정렬
    for k in graph:
        graph[k].sort()
        
    # print(graph)
    
    # dfs
    
    res = ["ICN"]
    found = False # 첫 경로 찾고나서 종료용 flag
    
    def dfs(level, v):
        nonlocal found
        
        if found:
            return
        
        if level == len(tickets):
            print("res : ", res)
            ans.extend(res)
            found = True
            return
        
        # print("v : ", v)
        if v in graph:
            for i in range(len(graph[v])):
                if not graph[v][i][1]:
                    graph[v][i][1] = True
                    res.append(graph[v][i][0])
                    # print("before : ", v)
                    # print("before graph : ", graph)
                    dfs(level+1, graph[v][i][0])
                    graph[v][i][1] = False
                    res.pop()
                    # print("after : ", v)
                    # print("after graph : ", graph)
    
    dfs(0, "ICN")
    
    return ans


# tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]

print(solution(tickets))
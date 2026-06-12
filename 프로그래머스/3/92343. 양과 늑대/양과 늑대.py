def solution(info, edges):
    answer = [0]
    visited=[False]*len(info)
    
    def dfs(sheep, wolf):
        answer[0]=max(answer[0], sheep)
        if wolf>=sheep:
            return
        
        for parent, child in edges:
            if visited[parent] and not visited[child]:
                visited[child]=True
                
                if info[child]==0:
                    dfs(sheep+1, wolf)
                else:
                    dfs(sheep, wolf+1)
                visited[child]=False
    visited[0]=True
    dfs(1,0)
    return answer[0]
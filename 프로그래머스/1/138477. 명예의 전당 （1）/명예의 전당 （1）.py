def solution(k, score):
    
    answer = []
    a=[]
    
    for i in score:
        
        a.append(i)
        a.sort()
        
        if len(a) > k:
            a.pop(0)
            
        answer.append(a[0])
    return answer
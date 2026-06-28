def solution(d, budget):
    sum = 0
    answer=0
    d.sort()
    for i in d:
        sum+=i
        if sum<=budget:
            answer+=1
    return answer
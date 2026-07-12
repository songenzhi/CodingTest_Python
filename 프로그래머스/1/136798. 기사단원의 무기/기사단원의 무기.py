def solution(number, limit, power):
    answer = 0
    
    for i in range(1, number+1):
        n = 0
        
        for j in range(1, int(i**0.5)+1):
            if i % j == 0:
                if j == i // j:
                    n += 1
                else:
                    n += 2
                
        if n > limit:
            n = power
            
        answer+=n
        
        
    return answer
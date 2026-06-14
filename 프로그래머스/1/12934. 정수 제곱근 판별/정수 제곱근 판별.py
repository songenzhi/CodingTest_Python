def solution(n):
    
    x = n ** 0.5
    
    if x==int(x):
        return int((x+1)**2)
    else:
        return -1
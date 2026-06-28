def solution(sizes):
    
    w =0 
    h=0
    for s in sizes:
        s.sort()
        w = max(w, s[0])
        h=max(h,s[1])
    
    return w*h
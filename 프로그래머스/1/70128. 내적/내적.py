def solution(a, b):
    ans = 0
    for c, d in zip(a,b):
        ans= ans+(c*d)
    return ans
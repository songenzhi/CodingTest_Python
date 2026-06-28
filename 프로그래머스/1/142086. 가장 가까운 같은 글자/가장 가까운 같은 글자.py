def solution(s):
#  딕셔너리 이용
    answer = []
    last = {}
    
    for i in range(len(s)):
        if s[i] in last:
            answer.append(i - last[s[i]])
        else:
            answer.append(-1)
            
        last[s[i]] = i
    return answer
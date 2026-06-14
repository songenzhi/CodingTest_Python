def solution(s):
    ans =[]
    
    if s[0]=="-":
        ans.append(s[0])
        for i in range(1, len(s)):
            ans.append(s[i])
            
    else:
        for i in range(0,len(s)):
            ans.append(s[i])
                
    joined_str="".join(ans)
    return int(joined_str)
def solution(babbling):
    words = ["aya", "ye", "woo", "ma"]
    answer = 0
    
    for b in babbling:
        idx = 0
        prev = ""
        
        while idx < len(b):
            found = False
            
            for word in words:
                if word != prev and b[idx:].startswith(word):
                    idx += len(word)
                    prev = word
                    found = True
                    break
            
            if not found:
                break
        if idx == len(b):
            answer += 1
    return answer
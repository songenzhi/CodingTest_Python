def solution(n, arr1, arr2):
    answer = []
    
    for a, b in zip(arr1, arr2):
        binary = bin(a | b)[2:].zfill(n)
        row = ""
        for c in binary:
            if c == "1":
                row += "#"
            else:
                row += " "
        answer.append(row)
    return answer
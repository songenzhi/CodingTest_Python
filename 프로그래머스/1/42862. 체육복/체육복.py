def solution(n, lost, reserve):
    lost = set(lost)
    reserve = set(reserve)
    
    # 1. 겹치는 애 제거
    common = lost & reserve
    lost -= common
    reserve -= common
    
    # 2. 빌려주기
    for r in sorted(reserve):
        if r - 1 in lost:
            lost.remove(r - 1)
        elif r + 1 in lost:
            lost.remove(r + 1)
    
    # 3. 결과
    return n - len(lost)
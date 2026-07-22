def solution(N, stages):
    answer = []
    tot_players=len(stages)
    
    for stage in range(1, N+1):
        if tot_players>0:
            fail_count = stages.count(stage)
            rate = fail_count/tot_players
            answer.append((stage, rate))
            tot_players -= fail_count
        else:
            answer.append((stage,0))
    answer.sort(key=lambda x:  x[1], reverse=True)
    return [stage for stage, rate in answer]
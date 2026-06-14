def solution(n):
    sorted_list = sorted(str(n), reverse=True)
    return int("".join(sorted_list))
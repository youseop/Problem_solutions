def solution(n, t, m, timetable):
    answer = ''
    for i in range(len(timetable)):
        h,mi = timetable[i].split(':')
        timetable[i] = int(h)*60 + int(mi)
    timetable.sort()

    bus_time = 540  # per t min
    bus_cnt = 1 # ~ n
    cru_cnt = 0 # max: m
    for time in timetable:
        full = 0
        if time <= bus_time:
            cru_cnt += 1
        else:
            while time>bus_time and bus_cnt <n:
                bus_time += t
                bus_cnt += 1
                cru_cnt = 1
        if cru_cnt == m:
            full = 1
            cru_cnt = 0
            bus_cnt += 1
            bus_time += t

        if bus_cnt > n:
            break
    if full:
        tmp_time = time - 1
    else:
        tmp_time = bus_time


    answer += str(tmp_time//600)
    answer += str((tmp_time%600)//60)
    answer += ':'
    answer += str((tmp_time%60)//10)
    answer += str((tmp_time%60)%10)
    return answer
def solution(n, t, m, timetable):
    def readable(time):
        return str(time//600)+str((time%600)//60)+':'+str((time%60)//10)+str((time%60)%10)

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

    if full: #버스가 가득 차면 마지막 사람보다 1분이라도 일찍 와야한다.
        tmp_time = time - 1
    else:
        tmp_time = bus_time

    return readable(tmp_time)
def solution(distance, rocks, n):
    def is_available(x):
        nonlocal distance, rocks, n

        point = 0
        del_chance = n

        for rock in rocks:
            if rock-point >= x:
                point = rock
                continue
            if del_chance <= 0:
                return False
            else:
                del_chance -= 1

        return True
    
    rocks.sort()
    rocks.append(distance)

    l,r,res = 0,distance,distance
    while l<=r:
        mid = (l+r)//2
        if is_available(mid):
            l = mid + 1
            res = mid
        else:
            r = mid - 1

    return res
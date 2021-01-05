def search(col, ld, rd, n):
    size = ((1 << n) - 1)
    count = 0

    if col == size:
        return 1

    slots = ~(col | ld | rd) & size
    while slots:
        bit = slots & -slots
        count += search(col | bit, (ld | bit) >> 1, (rd | bit) << 1, n)
        slots -= bit

    return count

def solution(n):
    return search(0, 0, 0, n)


print(solution(int(input())))
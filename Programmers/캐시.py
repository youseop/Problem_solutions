import sys
sys.stdin = open("text.txt","rt")
read=sys.stdin.readline

def solution(cacheSize, cities):
    answer = 0
    cache = {}

    if cacheSize == 0:
        return len(cities)*5

    for city in cities:
        city = city.upper()
        
        cache_index = 0

        if city not in cache:
            answer += 5
        else:
            cache_index = cache[city]
            answer += 1

        remove_list = []
        for key in cache.keys():
            if cache[key] >= cache_index:
                cache[key] -= 1
            if cache[key]==0:
                remove_list.append(key)
        for key in remove_list:
            cache.pop(key)
        cache[city] = cacheSize

    return answer

print(solution(3,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(3,["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
print(solution(0,["Jeju", "Pangyo", "NewYork", "newyork"]))
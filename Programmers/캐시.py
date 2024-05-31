from collections import deque


def solution(cacheSize, cities):
    time = 0
    caches = deque(maxlen=cacheSize)

    if cacheSize == 0:
        return 5 * len(cities)

    for i in cities:
        i = i.lower()
        if i in caches:
            caches.remove(i)
            caches.append(i)
            time += 1
        else:
            time += 5
            caches.append(i)

    return time

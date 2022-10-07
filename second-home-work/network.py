import heapq
import collections


def find_dist(net, k):
    que = [[0,k]]
    dist = collections.defaultdict()

    while que:
        time,node = heapq.heappop(que)

        if node not in dist:
            dist[node] = time
            for v,w in net[node]:
                heapq.heappush(que,[time + w,v])

    return dist


def networkDelayTime(times, n, k):
    net = collections.defaultdict(list)

    for u, v, w in times:
        net[u].append((v,w))

    dist = find_dist(net, k)

    if len(dist) == n:
        return max(list(dist.values()))

    return -1

if __name__ == "__main__":
    times = eval(input("Please input times in format [[], ..., []]:"))
    N = int(input("Please input N: "))
    X = int(input("Please input X: "))

    print('---------------------------')
    print('Result:', networkDelayTime(times, N, X)) 

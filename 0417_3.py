from collections import defaultdict
# 网络时延表：网络到其他节点的延迟
# 剩余业务容量表： 每个节点的剩余业务容量
# 逃生路径时延最小，逃生节点集各节点剩余容量总和容纳故障节点的业务量

n = 3 # 节点数目，第一行
flights = [[-1,5,-1,8],[5,-1,1,3],[-1,1,-1,4],[8,3,4,-1]] # 2到n+1行表示业务网络时延矩阵,[i][j]
rl = [10,20,15,25] # 2+n行表示剩余容量表
src = 2 # 3+n:故障节点编号
delay = 12  # 4+n,需要迁移的业务量

import heapq

def findEscapeNodes(n, flights, rl, src, delay):
    # 将-1替换为一个非常大的数来表示无法直接到达
    for i in range(n):
        for j in range(n):
            if flights[i][j] == -1:
                flights[i][j] = float('inf')

    # 使用Dijkstra算法找到从故障节点到所有其他节点的最短路径
    def dijkstra(src):
        dist = [float('inf')] * n
        dist[src] = 0
        queue = [(0, src)]
        while queue:
            cur_dist, u = heapq.heappop(queue)
            if cur_dist > dist[u]:
                continue
            for v in range(n):
                if flights[u][v] != float('inf') and dist[v] > dist[u] + flights[u][v]:
                    dist[v] = dist[u] + flights[u][v]
                    heapq.heappush(queue, (dist[v], v))
        return dist
    
    # 计算最短路径
    min_distances = dijkstra(src)
    print("min_distances",min_distances)

    candidate_nodes = []

    # 选择满足条件的逃生节点集合
    for i in range(n):
        if i == src:
            continue
        if min_distances[i] + rl[i] >= delay:
            candidate_nodes.append((min_distances[i], i))
    
    # 按距离从小到大排序，如果距离相同，按编号从小到大排序
    candidate_nodes.sort()
    print("candidate",candidate_nodes)
    
    # 组装结果
    result = [x[1] for x in candidate_nodes if x[0] == candidate_nodes[0][0]]
    return result

# 测试数据
n = 4 # 节点数目
flights = [[-1,5,-1,8],[5,-1,1,3],[-1,1,-1,4],[8,3,4,-1]] # 业务网络时延矩阵
rl = [10,20,15,25] # 剩余容量表
src = 2 # 故障节点编号
delay = 12  # 需要迁移的业务量

# 计算结果
escape_nodes = findEscapeNodes(n, flights, rl, src, delay)
print("逃生节点集合:", escape_nodes)


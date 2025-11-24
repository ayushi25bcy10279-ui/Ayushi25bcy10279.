# Road Traffic Managemaent System
from heapq import heappush, heappop
# Road Map
rm = {
    "A": {"B": 1, "C": 3},
    "B": {"A": 1, "D": 1},
    "C": {"A": 3, "D": 2},
    "D": {"B": 1, "C": 2, "E": 4},
    "E": {"D": 4}
}
start = "A"
end = "E"
print("ROAD TRAFFIC MANAGEMENT\n")
print(f"Find best routes from {start} to {end}\n")
# Breadth First Search
def bfs(a, b):
    q = [(a, [a])]
    c = set()
    while q:
        node, path = q.pop(0)
        if node == b:
            return path
        if node not in c:
            c.add(node)
            for x in rm[node]:
                q.append((x, path + [x]))
    return None
print("BFS Route (shortest in steps):")
print(bfs(start, end))
# Depth First Search
def dfs(a, b):
    st = [(a, [a])]
    visited = set()
    while st:
        node, path = st.pop()
        if node == b:
            return path
        if node not in visited:
            visited.add(node)
            for x in rm[node]:
                st.append((x, path + [x]))
    return None
print("\nDFS Route (explores deeper paths):")
print(dfs(start, end))
#A* SEARCH
def heuristic(a, b):
    return abs(ord(a) - ord(b))
def a_star(a, b):
    ol = []
    heappush(ol, (0, a, [a], 0))  
    visited = set()
    while ol:
        priority, node, path, rs = heappop(ol)
        if node == b:
            return path, rs
        if node in visited:
            continue
        visited.add(node)
        for bb, distance in rm[node].items():
            new_cost = rs + distance
            new_priority = new_cost + heuristic(bb, b)
            heappush(ol, (new_priority, bb, path + [bb], new_cost))
    return None, None
print("\nA* Route (shortest in distance):")
path, distance = a_star(start, end)
print("Path:", path)
print("Total Distance:", distance)

import sys
def input():
  return sys.stdin.readline().strip()

a, b = [int(i) for i in input().split()]

stops = [input() for _ in range(a)]
graph = {}
dists = {}
for i in range(b):
  tobi = input().split('-')
  if tobi[1] not in graph.keys():
    graph[tobi[1]] = []
  graph[tobi[1]].append(tobi[0])
  if tobi[0] not in graph.keys():
    graph[tobi[0]] = []
  graph[tobi[0]].append(tobi[1])

if "home" not in graph.keys():
    graph["home"] = []
if "Waterloo GO" not in graph.keys():
    graph["Waterloo GO"] = []

def OH_GOD_I_LOVE_RUNESCAPE(g, start, end):
    q = [[start]]
    visited = set()
    while q:
        runescape = q.pop(0)
        x = runescape[-1]
        if x == end:
            return runescape
        elif x not in visited:
            for k in g.get(x, []):
                q.append(list(runescape) + [k])
        visited.add(x)

I_LOVE_MY_GARBAGE_ACC = OH_GOD_I_LOVE_RUNESCAPE(graph, "home", "Waterloo GO")
print(str(len(I_LOVE_MY_GARBAGE_ACC) - 1) if I_LOVE_MY_GARBAGE_ACC else "RIP ACE")
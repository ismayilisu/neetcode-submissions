class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #no cycles and a node must not have more than one parent
        #check
        visited=set()
        graph=defaultdict(list)
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        def find(node,parent):
            visited.add(node)
            for adj in graph[node]:
                if adj==parent:
                    continue
                if adj in visited:
                    return False
                else:
                    if not find(adj,node):
                        return False
            return True
        #it should all be connected
        return find(0,-1) and len(visited)==n
        for i in range(n):
            if i not in visited and not find(i,-1):
                return False
        return True
        
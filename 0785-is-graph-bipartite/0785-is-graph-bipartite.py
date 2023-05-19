class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}
        for node in range(len(graph)):
            if node not in color:
                stack = [node]
                color[node] = 0
                while(stack):
                    cur = stack.pop()
                    for conn in graph[cur]:
                        if conn not in color:
                            stack.append(conn)
                            color[conn] = color[cur] ^ 1
                        elif color[conn] == color[cur]:
                            return False
        return True
def main():
    visited1 = set()
    visited2 = set()
    queue = []
    n = int(input('Enter the total number of nodes: '))
    graph = dict()

    for i in range(1,n+1):
        edges= int(input('Enter number of edges for {0} : '.format(i)))
        graph[i] = list()

        for j in range(1,edges+1):
            node = int(input("Enter the edge {} for node {} : ".format(j,i)))
            graph[i].append(node)
        
    
    print("DFS : ")
    dfs(visited1,graph,1)
    print("\n BFS : ")
    bfs(visited2,graph,queue,1)


def dfs(visited,graph,node):
    if node not in visited:
        print(node,end=' ')
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited,graph,neighbour)

def bfs(visited,graph,queue,node):
    visited.add(node)
    queue.append(node)
    
    while queue:
        s = queue.pop(0)
        print(s,end=' ')
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


main()
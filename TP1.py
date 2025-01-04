from collections import deque, defaultdict

class Graph:
    def __init__(self, v):
        self.V = v + 1  
        self.adj = defaultdict(list)  

    def add_edge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)

    def is_reachable(self, s, d):
        visited = [False] * self.V
        queue = deque([s])

        visited[s] = True

        while queue:
            current = queue.popleft()

            for neighbor in self.adj[current]:
                if neighbor == d:
                    return True
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

        return False


if __name__ == "__main__":
    
    g = Graph(7)
    g.add_edge(1, 2)
    g.add_edge(2, 5)
    g.add_edge(3, 6)
    g.add_edge(4, 6)
    g.add_edge(4, 7)

    
    try:
        u = int(input("Enter start node: "))
        v = int(input("Enter destination node: "))

        
        if g.is_reachable(u, v):
            print("True")
        else:
            print("False")
    except ValueError:
        print("Invalid input. Please enter integers only.")

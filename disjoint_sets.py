class DisjointSet:
    def __init__(self, n):
        # Initializing rank, parent, and size lists
        # n + 1 handles 1-based indexing smoothly
        self.rank = [0] * (n + 1)
        self.size = [1] * (n + 1)
        self.parent = list(range(n + 1))

    def find_u_par(self, node):
        """Finds the ultimate parent of a node with path compression."""
        if node == self.parent[node]:
            return node
        # Path compression happens here
        self.parent[node] = self.find_u_par(self.parent[node])
        return self.parent[node]

    def union_by_rank(self, u, v):
        ulp_u = self.find_u_par(u)
        ulp_v = self.find_u_par(v)
        
        if ulp_u == ulp_v:
            return
        
        if self.rank[ulp_u] < self.rank[ulp_v]:
            self.parent[ulp_u] = ulp_v
        elif self.rank[ulp_v] < self.rank[ulp_u]:
            self.parent[ulp_v] = ulp_u
        else:
            self.parent[ulp_v] = ulp_u
            self.rank[ulp_u] += 1

    def union_by_size(self, u,v):

        ulp_u = self.find_u_par(u)
        ulp_v = self.find_u_par(v)

        if ulp_v == ulp_u:
            return 
        
        if self.size[u] > self.size[v]:
            self.parent[ulp_v] = ulp_u
            self.size[u] += self.size[v]
        else:
            self.parent[ulp_u] = ulp_v
            self.size[v] += self.size[u]

if __name__ == "__main__":
    ds = DisjointSet(7)
    
    ds.union_by_size(1, 2)
    ds.union_by_size(2, 3)
    ds.union_by_size(4, 5)
    ds.union_by_size(6, 7)
    ds.union_by_size(5, 6)
    
    # Check if 3 and 7 are in the same set or not
    if ds.find_u_par(3) == ds.find_u_par(7):
        print("Same")
    else:
        print("Not same")

    ds.union_by_size(3, 7)

    # Check again after union
    if ds.find_u_par(3) == ds.find_u_par(7):
        print("Same")
    else:
        print("Not same")
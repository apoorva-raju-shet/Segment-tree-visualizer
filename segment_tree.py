class SegmentTree:
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build(0, 0, self.n - 1)

    # Build segment tree
    def build(self, node, start, end):
        if start == end:
            self.tree[node] = self.arr[start]
        else:
            mid = (start + end) // 2
            self.build(2*node+1, start, mid)
            self.build(2*node+2, mid+1, end)
            self.tree[node] = self.tree[2*node+1] + self.tree[2*node+2]

    # Print tree structure
    def print_tree(self):
        print("\nSegment Tree Structure:\n")
        level = 1
        i = 0
        while i < 2*self.n - 1:
            for j in range(level):
                if i + j < len(self.tree) and self.tree[i+j] != 0:
                    print(self.tree[i+j], end="  ")
            print()
            i += level
            level *= 2


# -------- MAIN ----------
arr = list(map(int, input("Enter array elements: ").split()))
st = SegmentTree(arr)
st.print_tree()
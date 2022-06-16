def manhattan(jam, row, col):
    print(jam)
    n = len(jam)
    visited = set()
    queue = [(0, 0,0)]
    while queue:
        r, c,dis = queue.pop(0)
        if r == row and c == col:
            return dis
        visited.add((r, c))
        for next_row, next_col in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
            if (0 <= next_row < n) and (0 <= next_col < n) and (next_row,next_col) not in visited and jam[next_row][next_col]==0:
                queue.append((next_row, next_col,dis+1))
    return -1

if __name__=='__main__':
    x=17276
    res=1
    for i in range(100):
        res*=((x-1)/x)
        x-=1
    print(1-res)


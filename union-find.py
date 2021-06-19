def find_root(D, x):    # D는 임의의 리스트, x는 target index
    p = D[x]
    while p != D[p]:    # fixed point에 도달할 때까지 tree를 거슬러올라감
        p = D[p]
    return p

def union(D, x, y):
    pa = find_root(D, x)    # x의 루트
    pb = find_root(D, y)    # y의 루트
    if pa != pb:    # 루트가 서로 다른 경우(서로 연결되어 있지 않은 경우)만 union이 가능
        # 번호가 낮은 루트를 번호가 높은 루트의 자식으로 편입시킨다.
        if (pa < pb): D[pa] = pb
        else: D[pb] = pa
 

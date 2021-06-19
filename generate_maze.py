import numpy as np
from bokeh.io import output_notebook, show
from bokeh.plotting import figure

def generate_maze(n, m):
    # 기본형 만들기
    maze = np.tile([[1, 2], [2, 0]], (n // 2 + 1, m // 2 + 1))  # https://numpy.org/doc/stable/reference/generated/numpy.tile.html
    maze = maze[:-1, :-1]                                       # 마지막 행과 마지막 열을 삭제한다.(인덱스가 음인 경우는 자료의 끝에서부터 순서를 세어준 것과 같다.)
    nodes = {(i, j): (i, j) for i, j in np.argwhere(maze == 1)} # https://numpy.org/doc/stable/reference/generated/numpy.argwhere.html 
                                                                # 값이 1인 셀의 좌표(0부터 (행 번호, 열 번호)로 정해짐)를 수집해서 key와 value가 같은 dictionary를 생성
                                                                # https://docs.python.org/3/tutorial/datastructures.html#dictionaries 
                                                                # {(0, 0): (0, 0), (0, 2): (0, 2), ...}
    edges = np.argwhere(maze == 2)                              # 값이 2인 셀의 좌표로 리스트를 생성
                                                                # [[0, 1], [0, 3], ...]

    # recursion으로 구현된 find
    def find(p, q):
        if p != nodes[p] or q != nodes[q]:                      # 두 노드의 루트가 같아야 종결
            nodes[p], nodes[q] = find(nodes[p], nodes[q])
        return nodes[p], nodes[q]
    
    np.random.shuffle(edges)    # kruskal의 방법을 적용할 edge 선택의 순서를 랜덤하게 뒤섞음
       
    for e1, e2 in edges:        # edges = [[0, 1], [0, 3], ...]에서 각 edge를 순회
        if e1 % 2:                                      # e1이 홀수인 경우(2로 나눈 나머지가 1=True)
            p, q = find((e1 - 1, e2), (e1 + 1, e2))     # (e1, e2) 셀의 위, 아래가 node이므로 그 둘의 루트를 찾아 각각 p, q라 함
        else:                                           # e1이 짝수인 경우
            p, q = find((e1, e2 - 1), (e1, e2 + 1))     # (e1, e2) 셀의 좌, 우가 node이므로 그 둘의 루트를 찾아 각각 p, q라 함
        maze[e1, e2] = p != q
        if p != q:              # e1과 e2가 연결되어 있지 않은 경우
            nodes[p] = q        # union: e1과 e2를 연결시킴
    return maze

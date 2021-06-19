# unionset 클래스의 정의 시작
class unionset:
    # 생성자(unionset 인스턴스가 만들어질 때 호출되어 필드를 초기화하는 메서드)
    def __init__(self, nodenum):
        '''
        self.parents = []
        for i in range(nodenum + 1):
            self.parents.append(i)
        '''
        self.parents = [i for i in range(nodenum + 1)]  # 인스턴스 변수(필드) 초기화: [1, 2, ..., nodenum]

    # 앞선 예시에서 find_root()과 같은 기능을 재귀함수로 구현하였다.
    def get_root(self, node):
        if self.parents[node] == node:   # 최종 parent(즉 root)인 경우 recursion 종료
            return node
        else:
            return self.get_root(self.parents[node]) # root가 아닌 경우에는 자신을 호출한다. root일 때까지 이러한 재귀호출 스택은 쌓이게 된다.

    # 앞선 예시에서 union()과 같은 기능을 하는 함수이다.
    def union_root(self, node1, node2):
        if node1 < node2:
            self.parents[node1] = node2
        else:
            self.parents[node2] = node1

# unionset 클래스 정의 끝


# 크루스컬 알고리즘 구현부분
def kruskal(graph):
    # 꼭짓점의 개수 nodenum 구하는 과정
    s = set(i[0] for i in graph)
    s.update(i[1] for i in graph)
    nodenum = len(s)

    union = unionset(nodenum)                       # unionset 인스턴스 생성
    sortededge = sorted(graph, key=lambda x: x[2])  # weight가 낮은 순서대로 정렬된 리스트를 얻는다. 정렬의 기준을 설정할 때 각 element의 3번째 element를 택하게끔 람다식을 활용하였다.
    sum = 0
    mst = []                                        # minimal spanning tree를 그리기 시작. 빈 리스트로 초기화
    for j in sortededge:                            # 각 edge를 순회(weight가 최소인 것부터 시작). 각각의 j는 길이 3인 리스트
        v1 = union.get_root(j[0])                   # j가 나타내는 edge의 한쪽 노드의 루트
        v2 = union.get_root(j[1])                   # j가 나타내는 edge의 반대쪽 노드의 루트
        if v1 != v2:                                # 루트끼리 다른 경우, 즉 아직 두 노드가 연결되어있지 않은 경우에만 다음을 실행한다.
            union.union_root(v1, v2)                # unionset의 메서드 union_root()를 실행하여 두 노드를 루트끼리 연결시킨다.
            sum += j[2]                             # weight의 sum을 나타낼 변수에 j가 나타내는 edge의 weight를 더한다.
            mst.append(j)                           # 결과로 반환할 mst 리스트에 j를 추가
    return mst, sum

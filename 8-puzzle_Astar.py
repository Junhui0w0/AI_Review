# 휴리스틱(경험적 탐색 기법)을 이용해 8-puzzle 구현
# 현재 상태와 목표 상태간의 차이(다른 부분의 갯수, 정답과의 거리 차이)를 이용해 탐색
# 차이가 작으면 작을수록 목표에 가까워지고 있다는 증거 == 차이가 크면 해당 방향으로는 탐색 X
# -> 더 빠른 속도로 탐색 가능

import queue

class State:
    def __init__(self, board, goal, depth=0):
        self.board = board
        self.goal = goal
        self.depth = depth

    def get_new_board(self, i1, i2, moves):
        new_board = self.board[:] # 기존 board 정보를 new_board에 복사
        new_board[i1], new_board[i2] = new_board[i2], new_board[i1] #index가 i1인 요소와 i2의 요소를 서로 스위칭
        return State(new_board, self.goal, moves) #새로운 상태 반환
    
    def expand(self, depth):
        result = []
        i = self.board.index(0) #요소가 0인 값의 index 반환

        if not i in [0,3,6]: #숫자0이 1열에 없다면
            result.append(self.get_new_board(i, i-1, depth)) #좌측으로 1칸 이동

        if not i in [0,1,2]: #숫자0이 1행에 없다면
            result.append(self.get_new_board(i, i-3, depth)) #위쪽으로 3칸 이동 (3x3이니 -3)

        if not i in [2,5,8]: #3열에 없다면
            result.append(self.get_new_board(i, i+1, depth)) #우측으로 1칸 이동
        
        if not i in [6,7,8]:
            result.append(self.get_new_board(i,i+3, depth)) #아래쪽으로 3칸 이동

        return result
    
    def f(self): #휴리스틱 계산
        return self.d() + self.c() #거리(distance) + 비용(cost)
    
    def d(self):
        score = 0

        for i in range(9):
            if self.board[i] != 0 and self.board[i] != self.goal[i]:
                score += 1

        return score
    
    def c(self):
        return self.depth
    
    def __eq__(self, other):
        return self.board == other.board
    
    def __ne__(self, other):
        return self.board != other.board
    
    def __str__(self):
        return f"f(n)={self.f()} // d(n)={self.d()} // c(n)={self.c()}\n" + str(self.board[:3]) + "\n" + str(self.board[3:6]) +"\n"+ str(self.board[6:]) + "\n=========="
    
    def __lt__(self, other):
        return self.f() < other.f()
    
    def __gt__(self, other):
        return self.f() > other.f()
    
puzzle = [2,8,3,
          1,6,4,
          7,0,5]

goal = [1,2,3,
        8,0,4,
        7,6,5]

open_q = queue.PriorityQueue()
open_q.put(State(puzzle, goal))

closed_q = []
depth = 0
cnt = 0

while not open_q.empty():
    cur = open_q.get()
    cnt += 1
    print(f"cnt = {cnt}")
    print(f"curent = {cur}")

    if cur.board == goal:
        print("성공")
        break

    depth = cur.depth + 1

    for state in cur.expand(depth):
        if state not in closed_q and state not in open_q.queue:
            open_q.put(state)
    
    closed_q.append(cur)

else:
    print("탐색 실패")

#===============================================================#
# A*는 Heuristic 이라고 하는 경험적 정보를 기반으로 한 탐색 기법이다.
# 8-puzzle에서 사용할 수 있는 경험적 정보는 현재 상태와 목표 상태간의 차이점이 있다.
# 해당 경험적 정보를 바탕으로 차이가 많이 나는 방향은 배제시킬 수 있으므로 탐색 속도가 높아진다.
# DFS로 구현한 방식보다 약 3배나 적은 시행횟수로 목표를 탐색할 수 있다.
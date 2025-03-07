# 탐색법으로는 크게 맹목적, 경험적 탐색 기법이 존재
# 맹목적: DFS, BFS
# 경험적: Greedy, A* (경험적 정보 == heuristic)
# 탐색에선 중복을 방지하기 위해 Open, Close List를 주로 사용


# [Game Board 구현(w.DFS)]
class State:
    def __init__(self, board, goal, depth = 0):
        self.board = board
        self.goal= goal
        self.depth = depth

    def get_new_board(self, i1, i2, moves):
        new_board = self.board[:] # 기존 board 정보를 new_board에 복사
        new_board[i1], new_board[i2] = new_board[i2], new_board[i1] #index가 i1인 요소와 i2의 요소를 서로 스위칭
        return State(new_board, self.goal, moves) #새로운 상태 반환
    
    def expand(self, depth):
        result = []
        if depth > 5: return result # 너무 깊이 빠지면 무한적으로 DFS가 수행될 수 있음.

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
    
    def __str__(self):
        return str(self.board[:3]) + "\n" + str(self.board[3:6]) +"\n"+ str(self.board[6:]) + "\n=========="
    
    def __eq__(self, other):
        return self.board == other.board
    
    def __ne__(self, other):
        return self.board != other.board
    
puzzle = [2, 8, 3,
          1,6,4,
          7,0,5]

goal = [1,2,3,
        8,0,4,
        7,6,5]

open_q = []
open_q.append(State(puzzle, goal))

closed_q = []
depth=0

cnt = 1
while len(open_q) != 0:
    cur = open_q.pop(0)
    print(f"cnt = {cnt}")
    cnt += 1
    print(f"cur = {cur}")

    if cur.board == goal:
        print("성공")
        break

    depth = cur.depth + 1
    closed_q.append(cur)

    if depth > 5:
        continue

    for state in cur.expand(depth):
        if (state in closed_q) or (state in open_q):
            continue
        else:
            open_q.append(state)


# ========================================================= #
# DFS(Depth First Search) 즉, 깊이 우선 탐색
# 한가지 경우의 수에 대해 끝없이 탐색
# Stack == LIFO == 가장 늦게 들어온 값이 가장 먼저 처리되어야 함
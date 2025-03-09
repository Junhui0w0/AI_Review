# 항상 최선의 수
# 턴 제 형식 게임, 반드시 승자와 패자 발생
# 해답이 존재할 경우 반드시 탐색된다

game_board = ['','','',
              '','','',
              '','','',]

def empty_cells(board):
    cells = []
    for x, cell in enumerate(board): #x는 index, cell은 value
        if cell == '':
            cells.append(x) #현재 value에 아무것도 없으면, x(인덱스)를 삽입
    return cells

def valid_move(x):
    return x in empty_cells(game_board) #x가 갈 수 있는지에 대한 True, False 반환

def move(x, player):
    if valid_move(x): #인자로 주어진 x로 갈 수 있다면 아래 블럭 수행
        game_board[x] = player #x번째 인덱스에 player 삽입
        return True
    return False

def draw(board):
    for i, cell in enumerate(board):
        if i % 3 == 0:
            print('\n------------')
        print('|', cell, '|', end='')
    print("\n------------")

def check_win(board, player):
    win_conf=[
        [board[0], board[1], board[2]],
        [board[3], board[4], board[5]],
        [board[6], board[7], board[8]],
        [board[0], board[3], board[6]],
        [board[1], board[4], board[7]],
        [board[2], board[5], board[8]],
        [board[0], board[4], board[8]],
        [board[2], board[4], board[6]],
    ]
    return [player, player, player] in win_conf #한 줄을 동일 player로 채워져 있으면 True를 반환

def evaluate(board):
    if check_win(board, 'X'):
        score = 1
    elif check_win(board, 'O'):
        score = -1
    else:
        score = 0
    return score

def game_over(board):
    return check_win(board, 'X') or check_win(board, 'O')

def minimax(board, depth, maxPlayer):
    pos = -1

    if depth == 0 or len(empty_cells(board)) == 0 or game_over(game_board): #게임이 종료되는 상황
        return -1, evaluate(board) 
    
    if maxPlayer: 
        value = -10000 #음의 무한대 

        for p in empty_cells(board): #board의 빈칸 index를 p에 반환
            board[p] = 'X'

            x, score = minimax(board, depth-1, False) #player를 False(O)로 변경 후 재귀
            board[p] = '' #board[p]에 X를 두기 전으로 회귀

            if score > value: #갱신
                value = score
                pos = p

    else:
        value = +10000 #양의 무한대

        for p in empty_cells(board):
            board[p] = 'O'

            x, score = minimax(board, depth-1, True)
            board[p] = ''
            
            if score < value:
                value = score
                pos = p

    return pos, value

player = 'X'
while True:
    draw(game_board)

    if len(empty_cells(game_board)) == 0 or game_over(game_board):
        break #빈칸이 없거나, 우승자가 가려진 경우 종료

    i, v = minimax(game_board, 9, player=='X')
    move(i, player)

    if player== 'X':
        player='O'
    else:
        player='X'

if check_win(game_board, 'X'):
    print('X 승리')
elif check_win(game_board, 'O'):
    print('O 승리')
else:
    print('비김')
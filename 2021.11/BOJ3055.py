from collections import deque
import sys

def isMoved(x, y, type, board):
    if type == "water":
        if x >= R or x < 0 or y >= C or y < 0 or board[x][y] == 'X' or board[x][y] == 'D' or board[x][y] == "*":
            return False
        else:
            return True

    elif type == "S":
        if x < R and x >= 0 and y < C and y >= 0 and (board[x][y] == '.' or board[x][y] == 'D'):
            return True
        else:
            return False


R, C = map(int, input().split())

# 위, 오른쪽, 아래, 왼쪽
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]

D = []
start = []
board = []
visited = [[False for _ in range(C)] for _ in range(R)]
start_water = deque()

for i in range(R):
    temp = input()
    for j in range(len(temp)):
        if temp[j] == 'D':
            D = [i, j]
        elif temp[j] == 'S':
            start = [i, j]
        elif temp[j] == '*':
            start_water.append([i, j])
            
    board.append(list(temp))

visited[start[0]][start[1]] = True

count = 0
move_q = deque()
move_q.append(start)


while True:
    if len(move_q) == 0:
        break

    size = len(start_water)
    for _ in range(size):
        cur_water = start_water.popleft()

        for d in direction:
            x = cur_water[0] + d[0]
            y = cur_water[1] + d[1]

            if isMoved(x, y, "water", board):
                board[x][y] = "*"
                start_water.append([x, y])
        
    size = len(move_q)
    for _ in range(size):
        cur = move_q.popleft()

        for d in direction:
            x = cur[0] + d[0]
            y = cur[1] + d[1]

            if [x,y] == D:
                count += 1
                print(count)
                sys.exit()

            if isMoved(x, y, "S", board):
                if not visited[x][y]:
                    visited[x][y] = True      
                    move_q.append([x,y])
        
    count += 1

print("KAKTUS")
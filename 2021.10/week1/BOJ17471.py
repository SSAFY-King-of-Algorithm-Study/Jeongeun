# 게리맨더링



# 서로 연결되어 있는지를 확인할 함수 하나
def isConnected(i, A_list, cnt, isVisited, N):
    if cnt == N:
        return

    temp_list = arr[i]

    for j in range(len(temp_list)):
        if temp_list[j] == 1 and j in A_list and not isVisited[j]:
            isVisited[j] = True
            isConnected(j, A_list, cnt+1, isVisited, N)


def combination(index, cnt, N):
    if cnt == N : return
    if index == N: return
    
    global minResult

    if cnt > 0:
        # 적어도 한개의 영역을 포함해야 하니까
        A_list = []
        B_list = []

        for i in range (N):
            if isSelected[i]:
                A_list.append(i)
            else:
                B_list.append(i)
        
        sumA = 0
        sumB = 0

        isVisitedA = [False for _ in range (N)]
        isVisitedB = [False for _ in range (N)]

        cntA = 0
        cntB = 0

        for i in A_list:
            isConnected(i, A_list, 0, isVisitedA, len(A_list))

        for i in A_list:
            if isVisitedA[i]:
                cntA += 1

        if cntA == len(A_list):
            for idx in A_list:
                sumA += population[idx]
        else:
            return
        
        for i in B_list:
            isConnected(i, B_list, 0, isVisitedB, len(B_list))

        for i in B_list:
            if isVisitedB[i]:
                cntB += 1
        
        if cntB == len(B_list):
            for idx in B_list:
                sumB += population[idx]
        else:
            return

        minResult = min(minResult, abs(sumA - sumB))

    isSelected[index] = True
    combination(index+1, cnt+1, N)

    isSelected[index] = False
    combination(index+1, cnt, N)



N = int(input())

population = list(map(int, input().split()))

arr = [[-1 for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i == j : arr[i][j] = 0
        else : arr[i][j] = -1

for i in range(N):
    input_list = list(map(int, input().split()))

    for j in range(1, len(input_list)):
        # 양뱡향 그래프
        arr[i][input_list[j]-1] = 1
        arr[input_list[j]-1][i] = 1

# 두개로 선거구를 나누는 방법

isSelected = [False for _ in range (N)]
location = [i for i in range (N)]

# 될 수 있는 최고 수 + 1
global minResult
minResult = 1001

combination(0, 0, N)


print(minResult)






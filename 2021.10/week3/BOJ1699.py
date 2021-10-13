# 제곱수의 합
import math
import sys


# 안됨!
def greedy(n):
    count = 0
    value = n

    while value != 0:
        root = int(math.sqrt(value))

        if int(math.pow(root,2)) == value:
            count += 1
            break
        else:
            value = value - int(math.pow(root,2))
            count += 1
        
    print(count)


def dp(n):
    memo = [0 for _ in range(n+1)]
    memo[1] = 1

    # 7 -> 2.xxx -> 2 
    # 7 - 4 = 3
    # 7 = 1 + memo[3] = 최소값이 아니면

    for i in range(2, n+1):
        root = int(math.sqrt(i))
        min = sys.maxsize

        while root > 0:
            value = i - int(math.pow(root,2))    
            if 1 + memo[value] < min:
                memo[i] = 1 + memo[value]
                min = memo[i]

            root -= 1

    print(memo[n])


if __name__ == "__main__":
    n = int(input()) 
    dp(n)

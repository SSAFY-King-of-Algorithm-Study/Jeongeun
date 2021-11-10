N = int(input())

# N번째에 해당하는 감소하는 수를 구하시오
# 0은 0번째 감소하는 수, 1은 1번째 감소하는 수
# 감소하는 수 항목에서 18번째로 감소하는 수는 42이다.

start = 0
number = 0

if N <= 10:
    print(N)
else:
    number = 20
    start = 10
    while start <= N:
        if number > 9876543210:
            number = 0
            break

        num_split = list(str(number))
        print(num_split)
        flag = True

        for i in range(0, len(num_split)):
            if i+1 < len(num_split):
                if num_split[i] > num_split[i+1]:
                    continue
                else:
                    num_split[i] = str(int(num_split[i]) + 1)
                    num_split[i+1] = str(0)
                    number = int(''.join(num_split))    # num_split -> split -> int
                    flag = False
                    break
            else:
                break
        
        if flag:
            start += 1
            number += 1
            
            if start == N:
                break

    print(number-1)
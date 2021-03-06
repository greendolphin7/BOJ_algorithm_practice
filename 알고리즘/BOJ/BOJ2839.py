# 설탕배달

N = int(input())

if N % 5 == 0:  # 만약에 처음 5로 나누어떨어지면 바로 종료
    print(N // 5)
else:
    count = 0  # 5로 나누어 떨어지지 않으면 최소한 나머지가 있다는 뜻

    while N > 0: 
        N -= 3  # 3부터 먼저 줄여나가면서 갯수 추가
        if N < 0:  # 3을 줄였는데 음수라는 건 5로도 나누어 떨어지지 않고 3으로도 뺄 수 없음
            print(-1)  # 바로 -1 출력하고 마무리
            break
        count += 1

        if N % 5 == 0:  # 3씩 줄여나가는데 중간에 5로 나누어 떨어지면 
            print(count + N // 5) # 출력하고 마무리
            break


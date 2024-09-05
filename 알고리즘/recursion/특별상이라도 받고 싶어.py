import sys
input = sys.stdin.readline

def divideQuarter(n, x, y):
    # 재귀적으로 4등분해서 각 구역의 2번째로 작은 값 찾기
    if n == 1:
        return seats[x][y]
    else:
        # 2차원 행렬을 4등분
        dividedSeats = [
            divideQuarter(n // 2, x, y),
            divideQuarter(n // 2, x, y + n // 2),
            divideQuarter(n // 2, x + n // 2, y),
            divideQuarter(n // 2, x + n // 2, y + n // 2)
        ]
        dividedSeats.sort()
        return dividedSeats[1]

if __name__ == "__main__":
    n = int(input().strip())
    seats = [list(map(int, input().split())) for _ in range(n)]
    print(divideQuarter(n, 0, 0))
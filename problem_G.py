import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    matrix = []
    for i in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    rowxor = [0] * n
    colxor = [0] * m

    for i in range(n):
        for j in range(m):
            x = matrix[i][j]
            rowxor[i] ^= x
            colxor[j] ^= x

    curr = sum(rowxor) + sum(colxor)
    ans = curr
    purngre = curr

    for i in range(n):
        ri = rowxor[i]
        for j in range(m):
            cj = colxor[j]
            old = matrix[i][j]
            A = ri ^ old
            B = cj ^ old
            best = A ^ B
            now = curr - ri - cj + best
            if now < ans:
                ans = now

    print(ans)

t = int(input())
for _ in range(t):
    a, v, l, n = map(int, input().split())
    
    if v == 1:
        print("NO")
    elif n >= a:
        print("NO") 
    else:
        print("YES")
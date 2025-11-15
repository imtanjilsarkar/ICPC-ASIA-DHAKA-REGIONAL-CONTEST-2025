t = int(input())

for i in range(t):
    nm = list(map(int, input().split()))
    n = nm[0]
    m = nm[1]
    
    arr = list(map(int, input().split())) 
    
    s = set(arr) 
    r = []  
    
    for j in range(m):
        x, y, z = map(int, input().split())
        r.append((x, y, z))
        
        if x in s and y in s:
            s.add(z)
    
    
    changed = True
    while changed:
        changed = False
        for x, y, z in r:
            if x in s and y in s and z not in s:
                s.add(z)
                changed = True
    
    print(len(s))
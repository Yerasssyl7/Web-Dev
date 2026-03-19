n = int(input())
a = list(map(int, input().split())) 

found = False

for i in range(len(a)):
    if a[i] == a[i-1] or a[i] == a[i+1]:
        found = True
        break

if found:
    print("YES")
else:
    print("NO")
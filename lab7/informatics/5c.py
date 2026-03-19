n = int(input())
a = list(map(int, input().split())) 
cnt = 0
for i in range(len(a)):
    if i > 0:
        cnt+=1
        print(cnt, end=" ") # end=" " позволяет печатать в одну строку
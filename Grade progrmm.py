n=int(input())
a=[]
for i in range(0,n):
    a.append(int(input()))
for j in range(0,n):
    if a[j] < 38:
        print(a[j])
    if a[j] >= 38:
        if ((a[j] % 5) > 2):
            a[j] +=5 - (a[j] % 5)
            print(a[j])
        elif ((a[j] % 5) <= 2):
            print(a[j])

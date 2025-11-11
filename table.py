# table.py 九九乘法表
def table(m,n):
    for i in range(1,m+1):
        for j in range(1, n+1):
            print(f"{i} * {j} = {i * j}", end=" ")
        print("\n")

table(9 , 9)
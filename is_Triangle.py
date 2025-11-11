# is_Triangle 判断是否为三角形
def is_Triangle(a, b, c):
    lst = [a ,b ,c]
    sorted(lst)
    if a + b < c:
        return False
    if c - a > b:
        return False
    return True

res = is_Triangle(4,4,4)
print(res)
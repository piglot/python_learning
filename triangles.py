
def triangles(n):
    res = [1]
    for i in range(n):
        yield res
        res_list = [res[i]+res[i+1] for i in range(len(res)-1)]
        res = [1] + res_list + [1]
        n = n + 1

for item in triangles(10):
    print(item)
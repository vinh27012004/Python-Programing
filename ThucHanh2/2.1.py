# Trả về danh sách nguyên tố của n
def lay_nguyen_to(n):
    nguyen_to = []
    for i in range(2, n + 1):
        while n % i == 0:
            nguyen_to.append(i)
            n //= i
    return nguyen_to

def tao_thua_so_nguyen_to(cac_so):
    thua_so_nguyen_to = {}
    for so in cac_so:
        thua_so_nguyen_to[so] = lay_nguyen_to(so)
    return thua_so_nguyen_to

# Nhập số nguyên dương
cac_so = list(map(int, input().split(',')))
thua_so_nguyen_to = tao_thua_so_nguyen_to(cac_so)
print(thua_so_nguyen_to)
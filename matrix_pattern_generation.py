m, n = map(int, input().split())
matrix = [['' for _ in range(n)] for _ in range(m)]
layers = min(m, n)//2+(min(m, n) % 2 != 0)
for layer in range(layers):
    if layer % 2 == 0:
        char = 'X'
    else:
        char = '0'

    for i in range(layer, n-layer):
        matrix[layer][i] = char
        matrix[m-layer-1][i] = char

    for j in range(layer, m-layer):
        matrix[j][layer] = char
        matrix[j][n-layer-1] = char

for i in matrix:
    print(" ".join(i))

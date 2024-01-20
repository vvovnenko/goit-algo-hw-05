from binary_search import binary_search

arr = [-4.56, -1, 0, 2, 7.56, 45, 78.1, 90, 100]

print('arr = ', arr)

for n in [-6, -4, -1, -0.5, 0, 1, 7.56, 34, 45.1, 78.1, 100, 101]:
    print(f'binary_search(arr, {n}) = ', binary_search(arr, n))

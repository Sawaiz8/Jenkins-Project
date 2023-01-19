import math
from random import randint

def dc(A, x, y, quadSize, key):
    newQuadSize = quadSize / 2

    if quadSize == 2:
        firstBox = 1 if A[x][y] == key else 0                 
        secondBox = 1 if A[x][y+1] == key else 0
        thirdBox = 1 if A[x+1][y] == key else 0
        fourthBox = 1 if A[x+1][y+1] == key else 0
    else:
        firstBox = dc(A, x, y, newQuadSize, key)
        secondBox = dc(A, x + quadSize//2, y, newQuadSize, key)
        thirdBox = dc(A, x, quadSize//2,newQuadSize, key) 
        fourthBox = dc(A, quadSize//2, quadSize//2, newQuadSize, key)
    return firstBox + secondBox + thirdBox + fourthBox

rows, cols = (4, 4)
A = [[randint(1,3) for i in range(cols)] for j in range(rows)]
print(A)
print(dc(A, 0, 0, rows, 4))

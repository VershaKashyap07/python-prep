##function to create matrxi
def createMatrix(rows, cols):
    # Initialize an empty matrix
    matrix = []

    # Define the number of rows and columns

    # Create the matrix
    for i in range(rows):
        res = []
        for j in range(cols):
            res.append(0)
        matrix.append(res)

    # Print the resulting matrix
    return matrix

## rotate matrxi by 90 degree
#i) brute force, only for square matrix

def roatateB(matrix,n,ans):
    for i in range(n):
        for j in range(n):
            ans[j][(n-1)-i] =  matrix[i][j]
    return ans

matrix = [[1,2,3],[4,5,6],[7,8,9]]

n = 3
ans  = createMatrix(3, 3)
print(ans)
print(roatateB(matrix,n,ans))

def rotateO(matrix,rows, cols):
    # for transpose
    for i in range(rows):
        for j in range(cols):
            matrix[i][j] = matrix[j][i]

    # to reverse the rows    
    for i in range(rows):
        left = 0
        right = cols - 1
        while left < right:
            matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
            left += 1
            right -= 1
            
    return matrix

print(rotateO(matrix,3,3))
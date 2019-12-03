"""
magic_squares.py
San Kwon IB CS HL Y1

This algorithm checks if a square is "magic".
An n x n matrix that is filled with the numbers 1, 2, 3…. n^2
is a magic square if the sum of the elements in each row, in
each column, and in the two diagonals is the same value. 

This is an adapted version of Ms. Richardson's starter pack.
Resources:
https://en.wikipedia.org/wiki/Magic_square
https://puzzling.stackexchange.com/questions/5933/how-to-determine-a-magic-constant-in-a-magic-square
"""

# This procedure prompts the user for n^2 inputs to populate a
# 2D square array which has alreay been declared
# precondition:  sqArr has been declared with a size of nxn
def fillSquare(n, sqArr):
    for r in range(n):
        print("----ROW " + str(r + 1) + "----")
        for c in range(n):
            sqArr[r][c] = int(input("Enter value: "))
    
# This procedure "pretty" prints a 2D square array of size n
def printSquare(n, sqArr):
    for r in range(n):
        for c in range(n):
            print(sqArr[r][c], end="\t")
        print("\n")

# This checks if the sum of the numbers in each row
#is equal to the magic number
def checkRow(n, sqArr, mNum):
    for r in range(n):
        rowsum = 0
        for c in range(n):
            rowsum = rowsum + sqArr[r][c]
        if rowsum != mNum:
                return False
    return True

# This checks if the sum of the numbers in each column is equal to the magic number
def checkCol(n, sqArr, mNum):
    for c in range(n):
        colsum = 0
        for r in range(n):
            colsum = colsum + sqArr[r][c]
        if colsum != mNum:
                return False
    return True

# This checks if the sum of the numbers in the
# left-to-right diagonal is equal to the magic number
def checkDiag1(n, sqArr, mNum):
    diagsum1 = 0
    for x in range(n):
        diagsum1 = diagsum1 + sqArr[x][x]
    if diagsum1 != mNum:
            return False
    return True

# This checks if the sum of the numbers in
# the right-to-left diagonal is equal to the magic number
def checkDiag2(n, sqArr, mNum):
    diagsum2 = 0
    for x in range(n):
        diagsum2 = diagsum2 + sqArr[n - x- 1][x]
    if diagsum2 != mNum:
            return False
    return True

# This checks if all the numbers are unique and
# consecutive with its smallest number being 1
def checkUnique(n, sqArr):
    checkArr1 = []
    for r in range(n):
        for c in range(n):
            checkArr1.append(sqArr[r][c])
    checkArr1.sort()
    checkArr2 = []
    for i in range(1, n ** 2 + 1):
        checkArr2.append(i)
    if checkArr1 != checkArr2:
        return False
    return True

# This checks if the square is a magic number
def checkSquare(size, square):
    magicNum = size * (size ** 2 + 1) / 2
    if(checkRow(size, square, magicNum) and  \
       checkCol(size, square, magicNum) and  \
       checkDiag1(size, square, magicNum) and  \
       checkDiag2(size, square, magicNum) and   \
       checkUnique(size, square)):
       return True
    else:
       return False


# This takes input from the user
# to determine the size of the square and the numbers in the square
s = int(input("Enter square side length:  "))
sq = [[0 for x in range(s)] for y in range(s)]
fillSquare(s, sq)

# This outputs whether the square is magic or not
printSquare(s, sq)
if checkSquare(s, sq):
    print("This is a magic square!")
else:
    print("This is not a magic square...")
   


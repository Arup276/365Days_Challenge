import numpy as np
print ("Enter the number of queens")
N = int(input())
s = (N,N)
board = np.zeros(s)# (nxn matrix initialize with zero)
def is_attack(i, j):
    #checking for row and column
    for k in range(0,N):
        if board[i][k]==1 or board[k][j]==1:
            return False
    #check diagonals
    for k in range(0,N):
        for l in range(0,N):
            if (k+l==i+j) or (k-l==i-j):
                if board[k][l]==1:
                    return False
    return True



def nqueen(n):
    if n==0:
        return True
    for i in range(0,N):
        for j in range(0,N):
            if (is_attack(i,j) and (board[i][j]!=1)):
                board[i][j] = 1
                if nqueen(n-1)==True:
                    return True
                board[i][j] = 0 # backtrack

    return False

nqueen(N)
for i in board:
    print (i)

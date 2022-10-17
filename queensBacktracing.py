

from numpy import true_divide


def queens(board,row=0):
    if row>len(board):
        return(True)
    
    for col in range(len(board)):
        if(isSafe(board,row,col)):
            board[row][col]=1
            if(queens(board,row+1)):
                return(true)
            board[row][col]=0
    return(False)

def isSafe(board,y,x):
    s=0
    for rows in range(len(board)):
        if rows==y:
            s+=sum(board[rows])
        else:
            s+=board[rows][x]

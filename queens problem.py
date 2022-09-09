N = int(input("type side of board: "))
n = N
count = 0


board = []
def build(board, N):
    for a in range(N):
        row = []
        for b in range(N):
            row.append("-")
        board.append(row)

def stampa(mat, N):
    for a in range(N):
        for b in range(N):
            print(mat[a][b], end=" ")
        print()
    print()


def valid(board, i, j, N):
    if 1 in board[i]:
        return False
    a = i
    b = j
    while(a>=0 and b>=0):
        if(board[a][b]==1):
            return False
        a=a-1
        b=b-1
    a = i
    b = j
    while(a<N and b<N):
        if(board[a][b]==1):
            return False
        a=a+1
        b=b+1
    a = i
    b = j
    while(a>=0 and b<N):
        if(board[a][b]==1):
            return False
        a=a-1
        b=b+1
    a = i
    b = j
    while(a<N and b>=0):
        if(board[a][b]==1):
            return False
        a=a+1
        b=b-1
    return True 
    
def insert(board, N, j):
    global count
    count += 1
    if j==N:
        return True 
    for i in range(N):
        if(valid(board,i,j,N)):
            board[i][j]=1
            if(insert(board, N, j+1)):
                return True
            board[i][j]="-"
    return False



build(board,N)
print(insert(board,N,0))
print("the fucntion called itself times: ", count)
stampa(board, N)
import math
#ketentuan file:
#karena kalo enter dibaca
#jadi baris terakhir juga harus dienter

#read maze from file
def readMaze():
    matrix=[]
    f = open("maze.txt", "r")
    for x in f:
        matrix.append(list(x)[:-1])
    return matrix

def bfs(matrix, visited, queue, start_x, start_y, finish_x, finish_y):
    arr = [start_x, start_y]
    queue_visited = []
    queue.append(arr)
    visited[start_x][start_y]=True
    while (queue[0][0]!=finish_x or queue[0][1]!=finish_y) :
        arr = queue[0]
        # print(arr)
        queue.pop(0)
        queue_visited.append(arr)
        if (arr[1]-1>0): #kiri posisi sekarang
            if(visited[arr[0]][arr[1]-1] == False):
                # print("kiri")
                visited[arr[0]][arr[1]-1] = True
                x = [arr[0], arr[1]-1]
                queue.append(x)
        if (arr[1]+1<len(visited)): #kanan posisi sekarang
            if(visited[arr[0]][arr[1]+1] == False):
                # print("kanan")
                visited[arr[0]][arr[1]+1] = True
                x = [arr[0], arr[1]+1]
                queue.append(x)
        if (arr[0]-1>0): #atas posisi sekarang
            if(visited[arr[0]-1][arr[1]] == False):
                # print("atas")
                visited[arr[0]-1][arr[1]] = True
                x = [arr[0]-1, arr[1]]
                queue.append(x)
        if (arr[0]+1<len(visited[0])): #bawah posisi sekarang
            if(visited[arr[0]+1][arr[1]] == False):
                # print("bawah")
                visited[arr[0]+1][arr[1]] = True
                x = [arr[0]+1, arr[1]]
                queue.append(x)
        # print(queue)
    arr = [finish_x, finish_y]
    queue_visited.append(arr)
    # print(queue_visited)
    return queue_visited

def countDistance(x, y, finish_x, finish_y):
    x = (finish_x-x)**2 + (finish_y-y)**2
    return math.sqrt(x)

# def astar(matrix, visited, queue, start_x, start_y, finish_x, finish_y):



if __name__ == "__main__":
    matrix = readMaze()
    # print(matrix)
    visited = [[False for x in range (len(matrix[0]))] for y in range (len(matrix))]
    for i in range (0, len(visited)):
        for j in range (0, len(visited[0])):
            if(matrix[i][j]=='1'):
                # print(i,j)
                visited[i][j]=True
    # print(visited)
    queue = []
    queue_visited = bfs(matrix, visited, queue, 1, 0, 9, 10)
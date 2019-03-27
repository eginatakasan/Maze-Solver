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
    return math.sqrt(10*(finish_x-x) + (finish_y-y)**2)

def astar(matrix, visited, queue, start_x, start_y, finish_x, finish_y):
    queue.append((start_x, start_y, 0, 0, 0))
    queue_visited=[]
    visited[start_x][start_y]=True
    while queue:
        visiting_idx=0
        for i in range (0,len(queue)): #cari f minimum
            if(queue[i][2]<queue[visiting_idx][2]):
                visiting_idx=i
        
        arr = queue[i]
        queue.pop(i)
        queue_visited.append((arr[0],arr[1]))

        if(arr[0]==finish_x and arr[1]==finish_y):
            print(queue_visited)
            return queue_visited
        
        for pos in [(0,-1), (0,1), (-1,0), (1,0)]:
            x = arr[0]+pos[0]
            y = arr[1]+pos[1]
            if x<0 or x>=len(visited[0]):
                continue
            if y<0 or y>=len(visited):
                continue
            if visited[x][y]==False:
                visited[x][y]=True
                h=countDistance(x,y,finish_x,finish_y)
                g=arr[3]+1
                f=g+h
                queue.append((x,y,f,g,h))


if __name__ == "__main__":
    matrix = readMaze()
    # print(matrix)
    visited1 = [[False for x in range (len(matrix[0]))] for y in range (len(matrix))]
    visited2 = [[False for x in range (len(matrix[0]))] for y in range (len(matrix))]
    for i in range (0, len(visited1)):
        for j in range (0, len(visited1[0])):
            if(matrix[i][j]=='1'):
                # print(i,j)
                visited1[i][j]=True
                visited2[i][j]=True
    # print(visited)
    queue = []
    #bfs
    # queue_visited = bfs(matrix, visited1, queue, 1, 0, 9, 10)
    # print(queue_visited)
    #astar
    astar(matrix, visited2, queue, 1, 0, 9, 10)
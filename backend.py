import math
#ketentuan file:
#karena kalo enter dibaca
#jadi baris terakhir juga harus dienter
class Node():
    def __init__(self,x,y,parent_x,parent_y):
        self.x = x
        self.y=y
        self.parent_x=parent_x
        self.parent_y=parent_y
    
    def search(self, q, x, y):
        for n in q:
            if(n.x==x and n.y==y):
                return n
            

#read maze from file
def readMaze():
    matrix=[]
    f = open("maze.txt", "r")
    for x in f:
        matrix.append(list(x)[:-1])
    return matrix

def bfs(matrix, visited, start_x, start_y, finish_x, finish_y):
    start = Node(start_x,start_y,None,None)
    queue=[]
    queue_visited = []
    queue.append(start)
    visited[start_x][start_y]=True
    while queue:
        arr = queue[0]
        # print(arr)
        queue.pop(0)
        queue_visited.append(arr)

        if arr.x==finish_x and arr.y==finish_y:
            path=[]
            current = arr
            while current.parent_x is not None:
                # print("jalan")
                path.append((current.x,current.y))
                # print(current.x, current.y, current.parent_x, current.parent_y)
                x=current.parent_x
                y=current.parent_y
                current = current.search(queue_visited, x, y)
                # print(current.x, current.y, current.parent_x, current.parent_y)
                # print (path[::-1])
            path.append((current.x,current.y))
            return path[::-1]

        for pos in [(0,-1), (0,1), (-1,0), (1,0)]:
            x = arr.x+pos[0]
            y = arr.y+pos[1]
            if x<0 or x>=len(visited[0]):
                continue
            if y<0 or y>=len(visited):
                continue
            if visited[x][y]==False:
                visited[x][y]=True
                child = Node(x,y,arr.x,arr.y)
                queue.append(child)

def countDistance(x, y, finish_x, finish_y):
    return abs(finish_x-x) + abs(finish_y-y)

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
    # queue = []
    #bfs
    queue_visited = bfs(matrix, visited1, 1, 0, 9, 10)
    print(queue_visited)
    #astar
    # astar(matrix, visited2, queue, 1, 0, 9, 10)
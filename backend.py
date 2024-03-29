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
def readMaze(file_name):
    matrix=[]
    f = open(file_name, "r")
    for x in f:
        matrix.append(list(x.strip()))
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
        # print(queue_visited[len(queue_visited)-1].x, queue_visited[len(queue_visited)-1].y)

        if arr.x==finish_x and arr.y==finish_y:
            # print("ketemu")
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
            # print(x,y)
            if x<0 or x>=len(visited):
                continue
            if y<0 or y>=len(visited[0]):
                continue
            if visited[x][y]==False:
                visited[x][y]=True
                child = Node(x,y,arr.x,arr.y)
                queue.append(child)

def countDistance(x, y, finish_x, finish_y):
    return abs(finish_x-x) + abs(finish_y-y)

def astar(matrix, visited, start_x, start_y, finish_x, finish_y):
    start=Node(start_x,start_y,None,None)
    #node, f, g, h
    queue=[]
    queue.append((start, 0, 0, 0)) 
    queue_visited=[]
    visited[start_x][start_y]=True
    while queue:
        imin=0
        for i in range (1,len(queue)): #cari f minimum
            if(queue[i][1]<queue[imin][1]):
                imin=i
        
        arr = queue[imin]
        queue.pop(imin)
        queue_visited.append(arr[0])

        if(arr[0].x==finish_x and arr[0].y==finish_y):
            path=[]
            current = arr[0]
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
            x = arr[0].x+pos[0]
            y = arr[0].y+pos[1]
            if x<0 or x>=len(visited[0]):
                continue
            if y<0 or y>=len(visited):
                continue
            if visited[x][y]==False:
                visited[x][y]=True
                child = Node(x,y,arr[0].x,arr[0].y)
                h=countDistance(x,y,finish_x,finish_y)
                g=arr[2]+1
                f=g+h
                queue.append((child,f,g,h))


def searchStart(matrix):
    for i in range (0, len(matrix)):
        if(matrix[i][0]=='0'):
            return i,0

def searchFinish(matrix):
    for i in range (0, len(matrix)):
        if (matrix[i][len(matrix)-1]=='0'):
            return i, (len(matrix)-1)

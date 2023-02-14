#Alexandros Panagiotakopoulos - alexandrospanag.github.io

from pyMaze import maze,agent,COLOR,textLabel
from collections import deque
def BFS(m):
    #repeat until Goal is reached or the frontier is empty
    start=(m.rows,m.cols)
    frontier=[start] #create the frontier[]
    explored=[start] #create the explored[]
    bfsPath={} #create the B F S path
    while len(frontier)>0:
        currCell=frontier.pop(0)
        if currCell==(1,1):
            break
        for d in 'ESNW': #for each direction:
            if m.maze_map[currCell][d]==True:
                #only one of the cases can be true!!
                if d=='E':  #if the direction is east, the child is on the east cell
                    childCell=(currCell[0],currCell[1]+1)
                elif d=='W': #if the direction is west, the child is on the west cell
                    childCell=(currCell[0],currCell[1]-1)
                elif d=='N': #if the direction is north, the child is on the north cell
                    childCell=(currCell[0]-1,currCell[1])
                elif d=='S': #if the direction is south, the child is on the south cell
                    childCell=(currCell[0]+1,currCell[1])
                if childCell in explored: #if childcell is already explored
                    continue #then do nothing
                frontier.append(childCell) #otherwise, the child cell will be appended
                explored.append(childCell) #append the child cell to the explored list
                bfsPath[childCell]=currCell #bfs path cell = current cell
    fwdPath={} #create the forward path (corresponds to out start-end cell)
    cell=(1,1) #cell 1.1 is the ending cell
    while cell!=start: #storing the bfs parth
        fwdPath[bfsPath[cell]]=cell
        cell=bfsPath[cell]
    return fwdPath

m=maze(10,10) #create a 10x10 maze
m.CreateMaze() #function to create the maze
path=BFS(m) #call the function

a=agent(m,footprints=True,filled=True) #creating a foot print to follow the created path
m.tracePath({a:path}) #tracking the path
l=textLabel(m,'Length of Shortest Path is:',len(path)+1) #lastly, print the length of the shortest path found!
m.run() #run the maze
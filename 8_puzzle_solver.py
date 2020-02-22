# -*- coding: utf-8 -*-

import numpy as np
import argparse
import time


## checking Location of Blank Tile
def blankTileLocation(state):
  for row,col in np.ndindex(state.shape):
      if state[row][col] == 0:
        return [row,col]


## function to move empty state left
def moveLeft(state,x,y):
    curr_state = np.copy(state)
    temp = curr_state[x,y-1]
    curr_state[x,y-1] = curr_state[x,y]
    curr_state[x,y] = temp
    return curr_state


## function to move empty state right
def moveRight(state,x,y):
    curr_state = np.copy(state)
    temp = curr_state[x,y+1]
    curr_state[x,y+1] = curr_state[x,y]
    curr_state[x,y] = temp
    return curr_state

## function to move empty state up
def moveUp(state,x,y):
    curr_state = np.copy(state)
    temp = curr_state[x-1,y]
    curr_state[x-1,y] = curr_state[x,y]
    curr_state[x,y] = temp
    return curr_state

## function to move empty state down
def moveDown(state,x,y):
    curr_state = np.copy(state)
    temp = curr_state[x+1,y]
    curr_state[x+1,y] = curr_state[x,y]
    curr_state[x,y] = temp
    return curr_state

# A node structure for our search tree
class Node: 
    # A utility function to create a new node
    # state : 3X3 array to reperesent puzzle board
    # index : to identify node
    # parent : pointer to parent node
    # left : pointer to left child
    # right : pointer to right child
    # up : pointer to up child
    # down : pointer to down child 

    def __init__(self, state,parent=None, index=0):
        self.state = state  
        self.parent = parent
        self.index = index
        self.left = None
        self.right = None
        self.up = None
        self.down = None

## function to check if a node has been visited before
def isVisited(state,visited) :
    flag = False
    for i in range(len(visited)):
        if np.array_equal(state,visited[i]):
            flag = True
            break
    return flag

# function to do level order search for goal state 
def searchLevelOrder(root,goalState): 
    # Base Case 
    if root is None: 
        return
    # Create an empty queue for level order traversal 
    queue = [] 
    visited = []
    # Enqueue Root 
    queue.append(root) 
    visited.append(root.state)

    nodes = open('Nodes.txt','w')
    nodesInfo = open('NodesInfo.txt','w')
    count = 0

    while(len(queue) > 0):
      node = queue.pop(0)
      if node is None:
          continue
      count += 1
      try :
          nodesInfo.writelines(str(count) + ' ' + str(node.index) + ' ' + str(node.parent.index) + '\n')
      except:
          nodesInfo.writelines(str(count) + ' ' + str(node.index) + ' ' + str(node.index) + '\n')
      nodes.writelines(str(node.state.flatten('F')).strip('[]') + '\n')

      if np.array_equal(node.state,goalState):
        print('Solution Found')
        pathPlanning(node)
        break 
    
      # Getting the location of blank tile
      [row,col] = blankTileLocation(node.state)

      # Enqueue left child
      if col>0:
        node.left = Node(moveLeft(node.state,row,col), parent=node, index=node.index + 1)
        if not isVisited(node.left.state,visited):
            visited.append(node.left.state)
            queue.append(node.left)

      # Enqueue right child
      if col<2:
        node.right = Node(moveRight(node.state,row,col), parent=node, index=node.index + 3)
        if not isVisited(node.right.state,visited):
            visited.append(node.right.state)
            queue.append(node.right)

      # Enqueue up child
      if row>0:
        node.up = Node(moveUp(node.state,row,col), parent=node, index=node.index + 2)
        if not isVisited(node.up.state,visited):
            visited.append(node.up.state)
            queue.append(node.up)

      # Enqueue down child
      if row<2:
        node.down = Node(moveDown(node.state,row,col), parent=node, index=node.index + 4)
        if not isVisited(node.down.state,visited):
            visited.append(node.down.state)
            queue.append(node.down)

    nodes.close()
    nodesInfo.close()

# Print nodes at a given level 
def pathPlanning(node):
    path = []
    curr_node = node
    while curr_node is not None:
        path.append(curr_node)
        curr_node = curr_node.parent
    path.reverse()
    with open('nodePath.txt','w') as f:
        for curr_node in path:
            f.writelines(str(curr_node.state.flatten('F')).strip('[]')+'\n')

## function to check solvability
def  isSolvable(state):
    inv_count = 0;
    curr_state = state.flatten()
    for i in range(9):
        for j in range(9):
             if curr_state[j] and curr_state[i] and curr_state[i] > curr_state[j]:
                  inv_count+=1
    return inv_count%2 == 0

## function to run puzzle-solver 
if __name__=='__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-s", "--start", required=False, help="Start array as a list (row-wise)",
                    default=np.random.permutation(9), nargs="*", type=int)
    args = vars(ap.parse_args())

    start_time = time.time()
    goal = np.append(np.arange(1, 9), 0).reshape((3, 3))
    start_state = np.array(args['start']).reshape((3, 3))

    start = Node(start_state)
    print('start is :', end='')
    print(start.state)
    print('goal is :', end='')
    print(goal)
    if isSolvable(start_state):
        print('Searching Solution...')
        searchLevelOrder(start, goal)
        print('time taken : ', end='')
        print(time.time()-start_time)
    else:
        print('Not Solvable')

# 8_puzzle_solver
This Project is intended to study different algorithms to find the optimum path to solve the 8-puzzle game in minimum number of steps.

At present, the solver uses Breadth-first search algorithm to search the state space to find the goal state and determines the optimal path from start to goal state.

## Dependencies

Following Dependencies are required:

1. Python3
2. Numpy

## Instructions

To run the file use the given command.
```
python 8_puzzle_solver.py

```
In the above case, the puzzle is solved for a start state chosen at random.


```
python 8_puzzle_solver.py -s <start-state>

```
Here, start-state is the list of numbers in the start state presented row-wise. 

## Output 
The 8_puzzle_solver.py generates 3 text files as output after it finds the goal state.

1. nodePath.txt :  List of states to follow to solve the puzzle presented as lists expanded column-wise


2. Nodes.txt : List of all the states explored in order to find the goal state, presented in column-wise list format


3. NodesInfo.txt : First Column --> Serial Number ; Second Column --> Node Index; Third Column --> Parent Node Index 

## Visualization

After the text files are generated, we can type this command to visualize results
```
python plot_path.py

```

This python script uses 'nodePath.txt' as input.  

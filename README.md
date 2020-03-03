# Sudoku

### About
Sudoku web app created by Rob Caporino. You can play sudoku normally by clicking on each cell and then the corresponding number you want to input. Normal sudoku rules apply, you must have a unique set of digits, 1 - 9, in each row, column, and each of the nine 3x3 smaller grids that make up the 9x9 larger one. The "check solution" button will check your input to see if it is correct.

### Backtrack Recursion
The "Solve with Backtracking" solves the entire puzzle with an algorithm and shows the algorithm going through its process. You can find the algorithm I used in the Board.vue file in src.

### Puzzle Generation
I wrote a python script to generate each puzzle for me. Each puzzle is based off of one starting puzzle with string values of a - i in each cell. The script randomizes which integer value, 1 - 9, corresponds to which string value and replaces them with that integer value. It then removes a number of cells from the puzzle symetrically.

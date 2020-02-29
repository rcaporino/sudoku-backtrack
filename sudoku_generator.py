import numpy as np
import random as rnd
import copy

startingBoards = np.array([
    [9,2,5,6,1,8,7,4,3],
    [1,3,4,2,5,7,8,6,9],
    [8,7,6,9,4,3,2,1,5],
    [7,6,1,3,9,2,5,8,4],
    [5,8,2,4,6,1,3,9,7],
    [3,4,9,8,7,5,1,2,6],
    [6,5,3,1,2,9,4,7,8],
    [4,1,7,5,8,6,9,3,2],
    [2,9,8,7,3,4,6,5,1]
])

def checkValid(board):
    # Check for duplicates in every row and col, check each row and col only once.
    for i in range(9):
        rd = board[i, :]
        cd = board[:, i]

        if(checkNotUnique(rd)):
            return False

        if(checkNotUnique(cd)):
            return False

    # Check for duplicates in each of the 9 3x3 sections
        blockRow, blockCol = divmod(i, 3)
        square = board[blockRow*3:(blockRow+1)*3, blockCol*3:(blockCol+1)*3]
        squareReshape = square.reshape(9)
        if(checkNotUnique(squareReshape)):
            return False
    return True

def checkNotUnique(lst):
    if(np.unique(lst).size < 9):
        return True
    return False    

# print(checkValid(startingBoards))

def countValids(boardLists):
    numValid = 0
    numNotValid = 0
    for b in boardLists:
        if(checkValid(b)):
            numValid+=1
        else:
            numNotValid+=1
    print("Valid: " + str(numValid))
    print("Not Valid: " + str(numNotValid))

def getRandomKeyValues():
    nums = list(range(1,10))
    keys = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
    rnd.shuffle(nums)
    rnd.shuffle(keys)

    keyValues = {keys[i] : nums[i] for i in range(9)}
    # keyValues = {{'id' : keys[i], 'val' : nums[i]} for i in range (9)}
    return keyValues

def resetBase():
    basePuzzle = [
        ["i","b","e","f","a","h","g","d","c"],
        ["a","c","d","b","e","g","h","f","i"],
        ["h","g","f","i","d","c","b","a","e"],
        ["g","f","a","c","i","b","e","h","d"],
        ["e","h","b","d","f","a","c","i","g"],
        ["c","d","i","h","g","e","a","b","f"],
        ["f","e","c","a","b","i","d","g","h"],
        ["d","a","g","e","h","f","i","c","b"],
        ["b","i","h","g","c","d","f","e","a"]
    ]
    return basePuzzle


def checkIfDuplicates_2(listOfElems):
    ''' Check if given list contains any duplicates '''    
    setOfElems = set()
    for elem in listOfElems:
        if elem in setOfElems:
            return True
        else:
            setOfElems.add(elem)         
    return False

def generatePuzzles():
    puzzles = []

    basePuzzle = [
        ["i","b","e","f","a","h","g","d","c"],
        ["a","c","d","b","e","g","h","f","i"],
        ["h","g","f","i","d","c","b","a","e"],
        ["g","f","a","c","i","b","e","h","d"],
        ["e","h","b","d","f","a","c","i","g"],
        ["c","d","i","h","g","e","a","b","f"],
        ["f","e","c","a","b","i","d","g","h"],
        ["d","a","g","e","h","f","i","c","b"],
        ["b","i","h","g","c","d","f","e","a"]
    ]

    for i in range(1000):
        newPuzzle = []
        keys = getRandomKeyValues()
        for r in basePuzzle:
            for k,v in keys.items():
                index = r.index(k)
                r[index] = v
            newPuzzle.append(r)
        puzzles.append(np.array(newPuzzle))
        basePuzzle = resetBase()
    
    countValids(puzzles)
 
generatePuzzles()


    

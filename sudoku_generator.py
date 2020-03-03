import random as rnd
import json

# generate random key value pairs for a-i and 1-9.
# this is done to help generate puzzles by replacing a puzzle of strings with new
# values
def getRandomKeyValues():
    nums = list(range(1,10))
    keys = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
    rnd.shuffle(nums)
    rnd.shuffle(keys)

    keyValues = {keys[i] : nums[i] for i in range(9)}
    return keyValues

# base puzzle all generated puzzles are based on
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

#remove 38 - 44 random cells from the puzzle symmetrically.
def removeNumbers(puzz):
    nToRemove = rnd.randrange(38, 45, 2)
    for i in range(nToRemove // 2):
        targetRow = rnd.randrange(0, 9)
        symRow = (9 - targetRow) - 1
        elToRemove = rnd.randrange(0, 9)
        symElToRemove = (9 - elToRemove) - 1
        if(puzz[targetRow][elToRemove] == 0):
            while(puzz[targetRow][elToRemove] == 0):
                targetRow = rnd.randrange(0, 9)
                symRow = (9 - targetRow) - 1
                elToRemove = rnd.randrange(0, 9)
                symElToRemove = (9 - elToRemove) - 1
        puzz[targetRow][elToRemove] = 0
        puzz[symRow][symElToRemove] = 0  
    return puzz     

# generates the puzzles
def generatePuzzles():
    puzzles = []
    basePuzzle = resetBase()
    for i in range(100):
        newPuzzle = []
        # get random key values to use
        keys = getRandomKeyValues()
        basePuzzle = resetBase()
        # for each row in the base puzzle
        for r in basePuzzle:
            # for each key value pair in keys
            for k,v in keys.items():
                # change the value of each index to the value of the corresponding index in keys
                index = r.index(k)
                r[index] = v
            newPuzzle.append(r)
        # remove cells from new puzzle
        newPuzzle = removeNumbers(newPuzzle)
        puzzles.append(newPuzzle)
    
    # write the puzzles to a json file.
    with open('puzzles.json', 'w') as f:
        json.dump(puzzles, f, ensure_ascii=False)

#commented out because I dont want to generate a new set of puzzles
# generatePuzzles()





    

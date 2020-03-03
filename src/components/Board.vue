<template>
  <div>
        <div class="row1" v-for="(row, rowIndex) in randomPuzzle" :key="rowIndex">
            <div class="cell" v-for="(cell, colIndex) in row" :key="colIndex" :class="{
                'cell-border-right': colIndex == 2 || colIndex == 5,
                'cell-border-bottom': rowIndex == 2 || rowIndex == 5,
                'cell-original': cell.original,
                'cell-active': activeRow == rowIndex && activeCol == colIndex,
                'cell-invalid': cell.value && checkCellInvalid(randomPuzzle, rowIndex, colIndex, cell.value)}"
                @click="setCellActive(rowIndex,colIndex, cell.original)">
                {{cell.value}}
            </div>
        </div>
        <br>
        <board-buttons :activeRow="activeRow"
            @settingCellValue="setCellValue($event)"
            @clearingBoard="clearBoard(true)" 
            @checkIfSolved="checkSolved"
            @solving="solving"
            @timerChange="changeTimer($event)">
        </board-buttons>
  </div>
</template>

<script>
// import Square from './Square.vue';
// import _ from 'lodash';
import Buttons from './Buttons.vue'
import puzzles from '../../puzzles.json'
export default {
    data() {
        return {
            myPuzzles: puzzles,
            randomPuzzle: [],
            rndIndex: 0,
            activeRow: -1,
            activeCol: -1,
            storeBacktrack: [],
            timer: 30,
            disableBacktrack: false,
            animation: []
        }
    },
    components: {
        boardButtons: Buttons
    },
    methods: {
        getRandomPuzzle() {
            this.rndIndex = Math.floor(Math.random() * this.myPuzzles.length);
            this.randomPuzzle = this.myPuzzles[this.rndIndex].map(row => {
                return row.map( cell => {
                    return {
                        value: cell !== 0 ? cell : null,
                        original: cell !== 0
                    }
                });
            });
            console.log('Puzzle #: ' + this.rndIndex)
            this.storeBacktrack = [];
            this.clearTimeouts();
        },
        setCellActive(row, col, original) {
            if(original) {
                return;
            }

            if(this.activeRow == row && this.activeCol == col) {
                this.activeRow = -1;
                this.activeCol = -1;
                return;
            }

            this.activeRow = row;
            this.activeCol = col;
        },
        setCellValue(value) {
            this.randomPuzzle[this.activeRow][this.activeCol].value = value
            this.storeBacktrack = [];
            this.clearTimeouts();
        },
        clearBoard(clearStoreBacktrack) {
            this.clearTimeouts();
            for(let r = 0; r < 9; r++) {
                for(let c = 0; c < 9; c++) {
                    if(this.randomPuzzle[r][c].original == false) {
                        this.randomPuzzle[r][c].value = null
                    }
                }
            }
            if(clearStoreBacktrack){
                this.storeBacktrack = [];
            }
        },
        checkCellInvalid(p, row, col, value) {
            for(let c = 0; c < 9; c++) {
                if(p[row][c].value == value && c != col) {
                    return true;
                }
            }

            for(let r = 0; r < 9; r++) {
                if(p[r][col].value == value && r != row) {
                    return true;
                }
            }

            var rowStart = Math.floor(row / 3) * 3;
            var colStart = Math.floor(col / 3) * 3;
            for(let r = rowStart; r < rowStart + 3; r++) {
                for(let c = colStart; c < colStart + 3; c++) {
                    if(p[r][c].value == value && !(r == row && c == col)) {
                        return true;
                    }
                }
            }
            return false;
        },
        checkSolved() {
            
            //check rows
            for(let r = 0; r < 9; r++) {
                let valueArray = []
                for(let c = 0; c < 9; c++) {
                    valueArray.push(this.randomPuzzle[r][c].value);
                    if(this.randomPuzzle[r][c].value == null){
                        alert("Not a Solution, error in row: " + (r + 1));
                        return false;
                    }
                }
                if(!this.checkUnique(valueArray)){
                    alert("Not a Solution, error in row: " + (r + 1));
                    return false;
                }
            }

            //check columns
            for(let r = 0; r < 9; r++) {
                let valueArray = []
                for(let c = 0; c < 9; c++) {
                    valueArray.push(this.randomPuzzle[c][r].value);
                }
                if(!this.checkUnique(valueArray)){
                    alert("Not a Solution, error in column");
                    return false;
                }
            }

            //check squares
            for(let r = 0; r < 9; r += 3) {
                for(let c = 0; c < 9; c += 3) {
                    let rowStart = Math.floor(r / 3) * 3;
                    let colStart = Math.floor(c / 3) * 3;
                    let square = this.getSquare(rowStart, colStart);
                    if(!this.checkUnique(square)) {
                        alert("Not a Solution, error in square: " + (rowStart + 1));
                        return false;
                    }
                }
            }
            alert("Correct Solution!");
            return true;
        },
        //get each of the smaller 3x3 squares in the grid.
        getSquare(rowStart, colStart){
            let square = [];
            for(let r = rowStart; r < rowStart + 3; r++) {
                for(let c = colStart; c < colStart + 3; c++) {
                    square.push(this.randomPuzzle[r][c].value);
                }
            }
            return square;
        },
        checkUnique(values) {
            if(new Set(values).size !== values.length){
                return false;
            }else{
                return true;
            }
        },
        solving(){
            this.disableBacktrack = true;
            if(this.checkSolved){
                this.storeBacktrack = [];
            }
            this.clearBoard(true);
            this.backtracking();
            this.clearBoard(false);
            this.displayAlg();
        },
        clearTimeouts() {
            for (let i = 0; i < this.animation.length; i++) {
                clearTimeout(this.animation[i]);
            }
        },
        numberUnassigned(row, col) {
            let numUnassign = null;
            let a = [];
            for(let r = 0; r < 9; r++) {
                for(let c = 0; c < 9; c++){
                    if(this.randomPuzzle[r][c].original == false && this.randomPuzzle[r][c].value == null) {
                        row = r;
                        col = c;
                        numUnassign = 1;
                        a = [row, col, numUnassign];
                        return a
                    }
                }
            }
            a = [-1, -1, numUnassign];
            return a;
        },
        backtracking() {
            let row = 0;
            let col = 0;
            //get check for the next cell to change
            let a = this.numberUnassigned(row, col);
            if(a[2] == null) {
                //if the grid is full stop
                return true;
            }
            row = a[0];
            col = a[1];

            for(let i = 1; i< 10; i++) {        
                //check i to see if it is a valid number to place in the current cell, if it is place it.            
                if(!this.checkCellInvalid(this.randomPuzzle, row, col, i)){
                    //setting cell value
                    this.randomPuzzle[row][col].value = i;
                    //used to animate the algorithm visually later
                    this.storeBacktrack.push({
                        'row': row,
                        'col': col,
                        'val': i
                    });

                    //recursion
                    if(this.backtracking()){
                        return true;
                    }
                    //if the number is no longer valid set it back to null and start down a different branch
                    this.randomPuzzle[row][col].value = null;
                    //used to animate the algorithm visually later
                    this.storeBacktrack.push({
                        'row': row,
                        'col': col,
                        'val': null
                    }); 
                }
            }
            return false;
        },
        //used to display the algorithm solving visually.
        displayAlg() {
            var that = this;
            for (let i = 0; i < this.storeBacktrack.length; i++) {
                (function(num){
                    that.animation.push(setTimeout(() => {
                        let r = that.storeBacktrack[i].row;
                        let c = that.storeBacktrack[i].col;
                        let val = that.storeBacktrack[i].val;
                        that.randomPuzzle[r][c].value = val;
                        if(i == that.storeBacktrack.length -1){
                            that.disableBacktrack = false;
                        }
                    }, that.timer * num))})(i);
            }

        },
        changeTimer(value) {
            this.timer = value;
        }
    },
    created() {
        this.getRandomPuzzle()
    }
}
</script>

<style>
.row1 {
    display: flex !important;
    align-items: center !important;
    justify-content: space-between !important;
}

.cell {
  display: block;
  width: 50px; height: 50px;
  box-sizing: border-box;
  border: 1px solid #bbb;
  font-size: 24px;
  line-height: 50px;
  text-align: center;
  cursor: pointer;
}

.cell:hover {
    background-color: #ddeeff;
}

.cell.cell-border-right {
    border-right-width: 3px;
    border-right-color: #000;
}
.cell.cell-border-bottom { 
    border-bottom-width: 3px; 
    border-bottom-color: #000;
}
.cell.cell-original { 
    font-weight: bold;
    cursor: default; 
}

.cell.cell.cell-original:hover {
    background-color: #fff;
}

.cell.cell-active {
    background-color: #bbdefb !important;
}

.cell.cell-invalid {
    background-color: #f00;
}
</style>
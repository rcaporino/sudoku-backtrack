<template>
  <div>
    <b-container>
      <b-row>
        <b-col>
          <b-card class="board mt-2 shadow">
            <b-row class="text-left" >
              <b-col>
                <h1>Sudoku</h1>
              </b-col>
            </b-row>
            <b-row class="text-left">
              <b-col>
                <p>
                  Sudoku web app created by Rob Caporino. You can solve puzzles manually by clicking on a cell and then which number you want to input. 
                  You can also click on the <strong>"Solve with Backtracking"</strong> button to watch the puzzles be solved using a recursive backtracking 
                  algorithm. Changing the slider changes the speed at which it solves.
                </p>
                <p>
                  View the source code <a href="https://github.com/rcaporino/sudoku-backtrack" target="_blank">here</a>
                </p>
              </b-col>
            </b-row>
            <hr>
            <b-row class="text-right pb-3">
              <b-col>
                <b-button style="width: fit-content;" variant="dark" @click="newPuzzle">
                  New Puzzle
                </b-button>
              </b-col>
            </b-row>
            <app-board ref="board"></app-board>
          </b-card>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import Board from './components/Board.vue';
  export default {
    components: {
      appBoard: Board
    },
    methods: {
      newPuzzle() {
        this.$refs.board.getRandomPuzzle();
      }
    }
  };
</script>

<style>
body{
  background-color: #efefef;
}

.shadow {
  box-shadow: 
    5px 5px 10px 1px rgba(0,0,0,0.3) !important;
}

@media (min-width: 768px) { 
  .board {
    width: calc(9 * 50px);
    margin: auto;
    padding: 2px;
  }
 }
</style>
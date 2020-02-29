<template>
  <div>
    <b-container>
      <b-row>
        <b-col>
          <b-card class="board mt-2">
            <!-- <app-square></app-square> -->
            <app-board></app-board>
          </b-card>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
// import Square from './components/Square.vue';
import Board from './components/Board.vue';
  export default {
    components: {
      // appSquare: Square,
      appBoard: Board
    }
  };
</script>

<style>
@media (min-width: 768px) { 
  .board {
    width: 500px;
    margin: auto;
    padding: 2px;
  }
 }
</style>
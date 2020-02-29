<template>
  <div>
      <b-row v-for="(squares, index) in groupedSquares" :key="index" no-gutters>
          <b-col  v-for="(s, index) in squares" :key="index">
              <component :is="s"></component>
          </b-col>
      </b-row>
  </div>
</template>

<script>
import Square from './Square.vue';
import _ from 'lodash';
export default {
    data() {
        return {
            fullBoard: []
        }
    },
    components: {
        bSquare: Square
    },
    computed: {
        groupedSquares() {
            return _.chunk(this.fullBoard, 3)
        }
    },
    methods: {
        generateBoard() {
            for(var i = 0; i < 9; i++){
                this.fullBoard.push("b-square");
            }
        }
    },
    created() {
        this.generateBoard();
    }
}
</script>

<style>

</style>
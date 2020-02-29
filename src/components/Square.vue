<template>
    <div class="square">
        <b-row v-for="(cells, index) in groupedCells" :key="index" no-gutters>
            <b-col v-for="(cell, index) in cells" :key="index">
                <b-cell :myNum="cell.num"></b-cell>
            </b-col>
      </b-row>        
    </div>
</template>

<script>
import Cell from './Cell.vue';
import _ from 'lodash';
export default {
    data() {
        return {
            cells: []
        }
    },
    components: {
        bCell: Cell
    },
    computed: {
        groupedCells() {
            return _.chunk(this.cells, 3)
        }
    },
    created() {
        this.generateCells();
    },
    methods: {
        generateCells() {
            let name = "appCell";
            let num;
            for(var i = 0; i < 9; i++){
                num = this.getRandom();
                this.cells.push({name: name, num: num})
                console.log(num);
            }
        },
        getRandom(){
            return Math.floor(Math.random() * (9 - 1)) + 1;
        }
    }
}
</script>

<style>
.square {
    border: 2px solid black !important;
    width:fit-content;
}
</style>
<template>
  <div>
        <b-row class="text-center" no-gutters>
            <b-col class="py-2 p-md-2" v-for="(n, i) in 9" :key="i">
              <b-button variant="primary" @click="setValue(n)" :disabled="isDisabled">
                  {{n}}
              </b-button>
            </b-col>
            <b-col class="py-2 p-md-2">
              <b-button  variant="warning" :disabled="isDisabled" @click="setValue(null)">
                  Clear<br>Cell
              </b-button>
            </b-col>
            <b-col class="py-2 p-md-2">
              <b-button style="" variant="danger" @click="clearBoard">
                  Clear Board
              </b-button>
            </b-col>
            <b-col class="py-2 p-md-2">
              <b-button style="" variant="success" @click="checkSolved">
                  Check Solution
              </b-button>
            </b-col>
        </b-row>
        <hr>
        <b-row class="text-center" no-gutters>
            <b-col>
                <b-button style="width: 100%;" variant="outline-danger"  @click="backtrackSolve">
                    Solve with Backtracking
                </b-button>
                <b-form-input class="my-3" id="range-1" v-model="timerValue" @input="timerChange(timerValue)" type="range" min="0" max="500"></b-form-input>
                Timer for backtrack iterations: {{timerValue}} milliseconds
            </b-col>
        </b-row>
    
  </div>
</template>

<script>
export default {
    data() {
        return {
            timerValue: 30
        }
    },
    props: [
        'activeRow',
    ],
    methods: {
        setValue(value){
            this.$emit('settingCellValue', value);
        },
        clearBoard() {
            this.$emit('clearingBoard');
        },
        checkSolved(){
            this.$emit('checkIfSolved');
        },
        backtrackSolve() {
            this.$emit('solving');
        },
        timerChange(value) {
            this.$emit('timerChange', value);
        }
    },
    computed: {
        isDisabled() {
            if(this.activeRow == -1){
                return true
            }else {
                return false
            }
        }
    }
}
</script>

<style>
button {
    width: 100px;
}
</style>
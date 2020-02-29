<template>
    <div>
        <b-form-input :no-wheel="wheel" :disabled="isDisabled" type="number" pattern="/^-?\d+\.?\d*$/"
            onKeyPress="if(this.value.length==1) return false;" :value="myNum"></b-form-input>
    </div>
</template>

<script>
export default {
    data() {
        return {
            isDisabled: false,
            wheel: true
        }
    },
    props: ['myNum']
}
</script>

<style>
input[type=number]::-webkit-inner-spin-button,
input[type=number]::-webkit-outer-spin-button {
    -webkit-appearance: none;
    margin: 0;
}
</style>
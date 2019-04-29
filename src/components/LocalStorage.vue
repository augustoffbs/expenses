<template>
<div>
    <button @click="setup">Setup</button>
    <button @click="setStorage">Local Storage</button>
    <button @click="delStorage">Delete Storage</button>
    <button @click="testLog">Test Log</button>
</div>
    
</template>

<script>
import expenses from '../App';
import uuid from 'uuid';

export default {
    name: "LocalStorage",
    methods: {
        setup() {
            var expenses = []
            localStorage.setItem("expenses", JSON.stringify(expenses))
            localStorage.setItem("total", "0")
        },
        setStorage() {
            var newStorage = {
                id: uuid.v4(),
                title: "test",
                amount: "test"
            }
            var exp = JSON.parse(localStorage.getItem("expenses"));
            exp.push(newStorage);
            localStorage.setItem("expenses", JSON.stringify(exp));
        },
        delStorage() {
            localStorage.clear()
        },
        testLog() {
            var values = localStorage.getItem("expenses");
            console.log(values);
        }
    }
}
</script>

<style scoped>

</style>


<template>
    <div>
        <h3>
            Testing buttons
        </h3>
        <div>
            <button @click="getExpenses">
                Get Expenses
            </button>
            <LocalStorage />
        </div>
    </div>
</template>

<script>
import LocalStorage from '../LocalStorage';


export default {
    name: "TestButtons",
    components: {
        LocalStorage
    },
    methods: {
        getExpenses() {
            var expenses = JSON.parse(localStorage.getItem("expenses"));
            for(var i = 0; i < expenses.length; i++) {
                return expenses[i].amount
            }
        }
    }
}
</script>

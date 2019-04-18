<template>
    <div>
        <form @submit="addExpense">
            <input type="text" v-model="title" name="title" placeholder="Add Expense...">
            <input type="text" v-model="amount" name="amount" placeholder="$">
            <input type="submit" value="Submit" class="btn">
        </form>
    </div>
</template>

<script>
import uuid from 'uuid';

export default {
    name: "AddExpense",
    data() {
        return {
            title: '',
            amount: ''
        }
    },
    methods: {
        addExpense(e) {
            const newExpense = {
                id: uuid.v4(),
                title: this.title,
                amount: this.amount,
                completed: false
            }
            this.$emit('add-expense', newExpense);
            this.title = '';
            this.amount = '';
        }
    }
}
</script>

<style scoped>
    form {
        display: flex;
    }

    input[type="text"] {
        flex: 10;
        padding: 5px;
    }

    input[type="submit"] {
        flex: 2;
    }

    input[name="amount"] {
        max-width: 20%;
    }
</style>



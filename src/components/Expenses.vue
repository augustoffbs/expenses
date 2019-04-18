<template>
    <div>
        <div v-bind:key="expense.id" v-for="expense in expenses">
            <div class="itemlist">
                <ExpenseItem v-bind:expense="expense" v-on:del-expense="$emit('del-expense', expense.id)"/>
            </div>
        </div>
    </div>
</template>

<script>
import ExpenseItem from './ExpenseItem.vue';

export default {
    name: "Expenses",
    components: {
        ExpenseItem
    },
    props: ["expenses"]
}
</script>

<style scoped>
.amount {
    float: right;
}
</style>

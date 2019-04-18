<template>
    <div class="expense-item" v-bind:class="{'is-complete':expense.completed}">
        <p>
            <input type="checkbox" v-on:change="markComplete">
            {{ expense.title }} // {{ expense.amount }}
            <button @click="$emit('del-expense', expense.id)" class="del">x</button>
        </p>
    </div>
</template>

<script>
export default {
    name: "ExpenseItem",
    props: ["expense"],
    methods: {
        markComplete() {
            this.expense.completed = !this.expense.completed;
        }
    }
}
</script>

<style scoped>

.expense-item {
    background: #f4f4f4;
    padding: 10px;
    border-bottom: 1px #ccc dotted
}

.is-complete {
    text-decoration: line-through;
}

.del {
    background: #ff0000;
    color: #fff;
    font-weight: bold;
    border: none;
    padding: 5px 9px;
    border-radius: 50%;
    cursor: pointer;
    float: right;
}

</style>

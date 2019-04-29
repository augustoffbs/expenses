<template>
    <div class="expense-item" v-bind:class="{'is-complete':expense.completed}">
        <p>
            {{ expense.title }} // ${{ expense.amount }}
            <button @click="$emit('del-expense', expense.id)" class="del" type="submit">x</button>
        </p>
    </div>
</template>

<script>
export default {
    name: "ExpenseItem",
    props: ["expense"]
}
</script>

<style scoped>

.expense-item {
    padding: 8px;
    border-bottom: 1px #ccc solid
}

.is-complete {
    text-decoration: line-through;
}

.del {
    width: 22px;
    height: 22px;
    float: right;
    border-radius: 50%;
    background: #d64b4b;
    color: #fff;
    font-weight: bold;
    border: none;
    cursor: pointer;
    margin: 0;
}

</style>

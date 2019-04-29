<template>
    <div class="expense-totals">
        <h3>
            Total:
            <span class="on-budget"> ${{ total }}</span>
        </h3>
    </div>
</template>

<script>
export default {
    name: "TotalExpenses",
    data() {
        var expenses = JSON.parse(localStorage.getItem("expenses"));
        var newTotal = 0;
        for(var i = 0; i < expenses.length; i++) {
            newTotal = newTotal + parseInt(expenses[i].amount);
            }
        localStorage.setItem("total", JSON.stringify(newTotal));
        return {
            total: newTotal
        }
    }
}
</script>

<style scoped>
.expense-totals {
    background: #f4f4f4;
    padding: 10px;
}

.on-budget {
    color: green;
}

.off-budget {
    color: red;
}
</style>

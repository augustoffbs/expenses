<template>
    <div class="expense-totals">
        <h3>
            Total:
            <span> $Total</span>
        </h3>
    </div>
</template>

<script>
export default {
    name: "TotalExpenses"
}
</script>

<style scoped>
.expense-totals {
    background: #f4f4f4;
    padding: 10px;
    border-bottom: 1px #ccc dotted
}
</style>

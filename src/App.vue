<template>
  <div id="app">
  <Header />
  <Expenses v-bind:expenses="expenses" v-on:del-expense="deleteExpense"/>
  </div>
</template>

<script>
import Header from './components/layout/Header';
import Expenses from './components/Expenses';

export default {
  name: 'app',
  components: {
    Header,
    Expenses
  },
  data() {
    return {
      expenses: [
        {
          id: 1,
          title: "Test one",
          amount: "$1500",
          completed: false
        },
        {
          id: 2,
          title: "Test two",
          amount: "$1500",
          completed: false
        },
        {
          id: 3,
          title: "Test three",
          amount: "$1500",
          completed: false
        }
      ]
    }
  },
  methods: {
    deleteExpense(id) {
      this.expenses = this.expenses.filter(expense => expense.id !== id)
    }
  }
}
</script>

<style>
  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  body {
    font-family: Arial, Helvetica, sans-serif;
    line-height: 1.4;
  }
</style>

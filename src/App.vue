<template>
  <div id="app">
  <Header />
  <AddExpense v-on:add-expense="addExpense" />
  <Expenses v-bind:expenses="expenses" v-on:del-expense="deleteExpense"/>
  </div>
</template>

<script>
import AddExpense from './components/AddExpense';
import Header from './components/layout/Header';
import Expenses from './components/Expenses';

export default {
  name: 'app',
  components: {
    AddExpense,
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
    },
    addExpense(newExpense) {
      this.expenses = [...this.expenses, newExpense]
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

  .btn {
    display: inline-block;
    border: none;
    background: #555;
    color: #fff;
    padding: 7px 20px;
    cursor: pointer;
  }

  .btn:hover {
    background: #666;
  }
</style>

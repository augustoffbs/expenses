<template>
  <div id="app">
  <Header />
  <LocalStorage />
  <AddExpense v-on:add-expense="addExpense" />
  <Expenses v-bind:expenses="expenses" v-on:del-expense="deleteExpense"/>
  </div>
</template>

<script>
import AddExpense from './components/AddExpense';
import Header from './components/layout/Header';
import Expenses from './components/Expenses';
import LocalStorage from './components/LocalStorage';
import axios from 'axios';

export default {
  name: 'app',
  components: {
    LocalStorage,
    AddExpense,
    Header,
    Expenses
  },
  data() {
    return {
      expenses: JSON.parse(localStorage.getItem("expenses"))
    }
  },
  methods: {
    deleteExpense(id) {
      // this.expenses = this.expenses.filter(expense => expense.id !== id)
      var delExp = JSON.parse(localStorage.getItem("expenses"));
      console.log(delExp);
      delExp = delExp.filter(expense => expense.id !== id);
      console.log(delExp);
      localStorage.setItem("expenses", JSON.stringify(delExp));
      location.reload()
    },
    addExpense(newExpense) {
      var addExp = JSON.parse(localStorage.getItem("expenses"))
      addExp.push(newExpense)
      console.log(addExp)
      localStorage.setItem("expenses", JSON.stringify(addExp));
    }
  },
  created() {
    // Get the local storage data
    //axios.get('https://my-json-server.typicode.com/augustoffbs/tracker/db')
    //.then(res => this.expenses = res.data);
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

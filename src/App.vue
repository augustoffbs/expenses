<template>
  <div id="app">
    <Header />
    <AddExpense v-on:add-expense="addExpense" />
    <Expenses v-bind:expenses="expenses" v-on:del-expense="deleteExpense"/>
    <TotalExpenses />
    <TestButtons />
  </div>
</template>

<script>
import AddExpense from './components/AddExpense';
import Header from './components/layout/Header';
import Expenses from './components/Expenses';
import TotalExpenses from './components/TotalExpenses';
import TestButtons from './components/layout/TestingButtons';

export default {
  name: 'app',
  components: {
    TestButtons,
    AddExpense,
    Header,
    Expenses,
    TotalExpenses
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
      delExp = delExp.filter(expense => expense.id !== id);
      localStorage.setItem("expenses", JSON.stringify(delExp));
      location.reload();
    },
    addExpense(newExpense) {
      var addExp = JSON.parse(localStorage.getItem("expenses"));
      addExp.push(newExpense);
      window.localStorage.setItem("expenses", JSON.stringify(addExp));
    }
  },
  //created() {
    // Get the local storage data
    //axios.get('https://my-json-server.typicode.com/augustoffbs/tracker/db')
    //.then(res => this.expenses = res.data);
  //}
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
    background: #90b9ad;
    color: #fff;
    padding: 7px 20px;
    cursor: pointer;
  }

  .btn:hover {
    background: #80a49a;
  }
</style>

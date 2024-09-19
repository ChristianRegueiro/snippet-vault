<template>
    <nav class="navbar" role="navigation" aria-label="main navigation">
      <div class="navbar-brand">
        <div id="navbarDiv" class="navbar-menu">
          <div class="navbar-start">
            <RouterLink to="/" class="button">Home</RouterLink>
            <RouterLink to="/snippets" class="button">Snippets</RouterLink>
            <RouterLink to="/add" class="button">Add</RouterLink>
          </div>
        </div>
      </div>
    </nav>
  </template>
  
  <script setup lang="ts"></script>
  
  <style scoped>
  .navbar {
    border-bottom: 1px solid #dbdbdb;
    padding: 1em;
  }
  .button {
    margin-right: 1em;
  }
  </style>
  
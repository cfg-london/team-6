<template>
  <div id="app">
    <nav>
      <div class="nav-wrapper">
        <!-- <a href="#" class="brand-logo">Logo</a> -->
        <ul id="nav-mobile" class="right hide-on-med-and-down">
          <li><router-link to='/'>Home</router-link></li>
          <li><router-link to='/nobel_prizes'>Nobel Prizes and Laureates</router-link></li>
          <li><router-link to='/nomination'>Nomination</router-link></li>
          <li><router-link to='ceremonies'>Ceremonies</router-link></li>
          <li><router-link to='/alfred_nobel'>Alfred Nobel</router-link></li>
          <li><router-link to='/education'>Educational</router-link></li>
          <li><router-link to='/events'>Events</router-link></li>
        </ul>
      </div>
    </nav>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'app'
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>

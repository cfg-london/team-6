<template>
  <div id="app">
    <nav>
      <div class="nav-wrapper">
        <!-- <a href="#" class="brand-logo">Logo</a> -->
        <!-- <div>
          <router-link to='/'>Nobel Prize</router-link>
        </div> -->
        
        <img src="../static/images/logo.png" />

        <ul id="nav-brand" class="right hide-on-med-and-down" style="padding-right:40px">
          <li><router-link to='/'>Home</router-link></li>
          <li><router-link to='/discover'>Discover</router-link></li>          
          <li><router-link to='/nobel_prizes'>Laureates</router-link></li>
          <li><router-link to='/nomination'>Nominations</router-link></li>
          <li><router-link to='ceremonies'>Ceremonies</router-link></li>
          <li><router-link to='/alfred_nobel'>About</router-link></li>
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
  text-align: left;
  color: #2c3e50;
}

nav {
  background-color: white;
}

nav ul a {
  color: black;
}

nav img {
  padding-left: 40px;
}

#app {
  background-color: black;
}

</style>

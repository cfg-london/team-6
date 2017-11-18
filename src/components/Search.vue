<template>
  <div class="container">
    <div class="nav-wrapper">
      <form>
        <div class="input-field">
          <input id="search" type="search" required>
          <label class="label-icon" for="search"><i class="material-icons">search</i></label>
          <i class="material-icons">close</i>
        </div>
      </form>
    </div>
    <div class="left">
      <a href="#">
        <table>
          <tr>
            <td rowspan="2">
              <img src="albert.jpg" alt="Albert Museum" />
            </td>
            <td>
              (name from back end)
            </td>
          </tr>
          <tr>
            <td>
              (everything else from backend)
            </td>
          </tr>
        </table>
      </a>
    </div>
    <div class="white right">
      Relevant information
    </div>
  </div>
</template>

<script>
export default {
  name: 'Search',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
.landing {
  background-color: black;
  height: 100vh;
  color: white;
}

.image {
  display: inline-block;
}

.wrapper {
  text-align: center;
}

.image img {
  width: 30%;
}

.image-wrapper img {
  width: 40%;
}

.image-wrapper {
  padding: 100px 0;
}

.col h1 {
  margin: 200px 0;
}

.image, .explanation {
  display: inline-block;
  width: 50vw;
  height: 80vh;
}

.landing {
  width: 100%;
  font-family: "Roboto Mono", monospace;
}
th, td {
    color: #FFF;
    padding: 15px;
    text-align: center;
}

.nav-wrapper {
  position: fixed;
}

#search {
  font-size: 30px;
}

table {
  margin: 70px 0 0 0;
}

.container {
  height: 300vh;
}
</style>

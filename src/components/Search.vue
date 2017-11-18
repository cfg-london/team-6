<template>
  <div class="container search-div">
    <div class="nav-wrapper">
      <form>
        <div class="input-field">
          <input id="search" type="search" v-on:submit.prevent="search" v-on:keyup.enter="search" v-model="query" required>
          <label class="label-icon" for="search"><i class="material-icons">search</i></label>
          <i class="material-icons">close</i>
        </div>
      </form>
    </div>
    <div class="left" :class="{ hidden: isHiden }">
      <a href="#">
        <name-card :laureate-name="name" :image-url="imageUrl" :link="wikiLink">
        </name-card>
      </a>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Search',
  data () {
    return {
      query: "",
      msg: 'Welcome to Your Vue.js App',
      name: '',
      firstResult: '',
      imageUrl: '',
      wikiLink: '',
      isHiden: true
    }
  },
  methods: {
    search () {
      console.log("search query been submitted")
      this.$http.get('http://34.230.141.99:5002/search/' + this.query + '/1')
      .then(function(res) {
        console.log(res.body);
        this.firstResult = res.body[0];
        this.imageUrl = this.firstResult.image_link;
        this.name = this.firstResult.firstname + ' ' + this.firstResult.surname;
        this.wikiLink = this.firstResult.wiki_link;
        this.isHiden = false;
      }, function(error) {
      })
    }
  } 
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.search-div {
  height: 100vh !important;
}

.hidden {
  visibility: hidden;
}

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

.container {
  height: 100%;
}

.left {
  margin: 100px 0 0 0;
}

.input-field input {
  /* background-color:  */
}
</style>

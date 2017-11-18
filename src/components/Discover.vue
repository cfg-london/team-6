<template>
  <div class="container">
    <span style="color: #ffffff; display: block; padding: 10px; text-align: center;">
      Nine Nobel Prize laureates who have changed the world - click on their links to find out more!
    </span>
    <!-- <div class="row">
      <div class="col-xs-12 col-sm-4">
        <a href="">
          <name-card laureate-name="Albert Einstein" image-url="https://www.nobelprize.org/nobel_prizes/physics/laureates/1921/einstein_postcard.jpg">
          </name-card>
        </a>
      </div>
      <div class="col-xs-12 col-sm-4">
        <a href="">
          <name-card laureate-name="Albert Einstein" image-url="https://www.nobelprize.org/nobel_prizes/physics/laureates/1921/einstein_postcard.jpg">
          </name-card>
        </a>
      </div>
      <div class="col-xs-12 col-sm-4">
        <a href="">
          <name-card laureate-name="Albert Einstein" image-url="https://www.nobelprize.org/nobel_prizes/physics/laureates/1921/einstein_postcard.jpg">
          </name-card>
        </a>
      </div>
    </div>
    <div class="row">
      <div class="col-xs-12 col-sm-4">
        <a href="">
          <name-card laureate-name="Albert Einstein" image-url="https://www.nobelprize.org/nobel_prizes/physics/laureates/1921/einstein_postcard.jpg">
          </name-card>
        </a>
      </div>
      <div class="col-xs-12 col-sm-4">
        <a href="">
          <name-card laureate-name="Albert Einstein" image-url="https://www.nobelprize.org/nobel_prizes/physics/laureates/1921/einstein_postcard.jpg">
          </name-card>
        </a>
      </div>
      <div class="col-xs-12 col-sm-4">
        <a href="">
          <name-card laureate-name="Albert Einstein" image-url="https://www.nobelprize.org/nobel_prizes/physics/laureates/1921/einstein_postcard.jpg">
          </name-card>
        </a>
      </div>
    </div>
    <div class="row">
      <div class="col-xs-12 col-sm-4">
        <a href="">
          <name-card laureate-name="Albert Einstein" image-url="https://www.nobelprize.org/nobel_prizes/physics/laureates/1921/einstein_postcard.jpg">
          </name-card>
        </a>
      </div>
      <div class="col-xs-12 col-sm-4">
        <a href="">
          <name-card laureate-name="Albert Einstein" image-url="https://www.nobelprize.org/nobel_prizes/physics/laureates/1921/einstein_postcard.jpg">
          </name-card>
        </a>
      </div>
      <div class="col-xs-12 col-sm-4">
        <a href="">
          <name-card laureate-name="Albert Einstein" image-url="https://www.nobelprize.org/nobel_prizes/physics/laureates/1921/einstein_postcard.jpg">
          </name-card>
        </a>
      </div>
    </div> -->

    <div class="row">
      <div class="col-xs-12 col-sm-4" v-for="result in results">
          <name-card :laureate-name="result.firstname" :image-url="result.image_link" :link="result.wiki_link">
          </name-card>
      </div>

    </div>
    

  </div>
</template>

<script>
export default {
  name: 'Discover',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      results: []
    }
  },
  created: function() {
      console.log("search query been submitted")
      this.$http.get('http://34.230.141.99:5002/random/9')
      .then(function(res) {
        console.log(res.body);
        this.results = res.body.Random;
        // this.imageUrl = this.firstResult.image_link;
        // this.name = this.firstResult.firstname + ' ' + this.firstResult.surname;
        // this.wikiLink = this.firstResult.wiki_link;
      }, function(error) {
      })
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

.container[data-v-abffd2d8] {
    height: 100%;
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

.row h3 {
  color: white;
}

.row img {
  width: 100%;
}
</style>

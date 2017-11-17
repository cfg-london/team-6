<template>
  <div class="container landing">
    <div id="myCarousel" class="carousel slide" data-ride="carousel">
  <!-- Indicators -->
  <ol class="carousel-indicators">
    <li data-target="#myCarousel" data-slide-to="0" class="active"></li>
    <li data-target="#myCarousel" data-slide-to="1"></li>
    <li data-target="#myCarousel" data-slide-to="2"></li>
  </ol>

  <!-- Wrapper for slides -->
  <div class="carousel-inner">
    <div class="item active">
      <div class="container">
        <div class="image-wrapper">
          <img src="http://nobelcenter.se/wp-content/uploads/2017/10/nobelcenter_Water_night_webb-portrait.jpg" alt="nobel center">
        </div>
        <div class="caption-wrapper">
          <h1>Nobel Prize Center</h1>
        </div>
      </div>
    </div>

    <div class="item active">
      <img src="https://www.smashingmagazine.com/wp-content/uploads/2015/06/10-dithering-opt.jpg" alt="Chicago">
    </div>

    <div class="item">
      <img src="https://www.smashingmagazine.com/wp-content/uploads/2015/06/10-dithering-opt.jpg" alt="New York">
    </div>
  </div>

  <!-- Left and right controls -->
  <a class="left carousel-control" href="#myCarousel" data-slide="prev">
    <span class="glyphicon glyphicon-chevron-left"></span>
    <span class="sr-only">Previous</span>
  </a>
  <a class="right carousel-control" href="#myCarousel" data-slide="next">
    <span class="glyphicon glyphicon-chevron-right"></span>
    <span class="sr-only">Next</span>
  </a>
</div>
    <div class="row">
      <div class="col image-wrapper">
        <img src="http://nobelcenter.se/wp-content/uploads/2017/10/nobelcenter_Water_night_webb-portrait.jpg" alt="nobel center">
      </div>
      <div class="col">
        <h1>Nobel Prize Center</h1>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
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

.caption-wrapper {
  width: 50%;
  float: left;
}

.image-wrapper {
  width: 50%;
  float: left;
}

#myCarousel {
  height: 80vh;
}
</style>

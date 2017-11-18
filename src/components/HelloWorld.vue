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
          <img src="https://pbs.twimg.com/media/DMBRXyBXcAApx-T.jpg:large" alt="nobel">
        </div>
        <div class="caption-wrapper">
          <h3>Discover the artist behind the striking illustrations of the new Nobel Laureates: Niklas Elmehed!</h3>
        </div>
      </div>
    </div>

    <div class="item">
      <div class="container">
        <div class="image-wrapper">
          <img src="https://scontent-lhr3-1.xx.fbcdn.net/v/t31.0-8/23157201_10155067285644103_7306413616051286343_o.jpg?oh=c2a4d49d519090246532e3292b7668c0&oe=5AA50350" alt="Marie Curie">
        </div>
        <div class="caption-wrapper">
          <h3>Happy birthday to Marie Curie, née Sklodowska, who was born 150 years ago on this day!</h3>
        </div>
      </div>
    </div>

    <div class="item">
      <div class="container">
        <div class="image-wrapper">
          <img src="https://scontent-lhr3-1.xx.fbcdn.net/v/t1.0-9/22528529_10155031777039103_833504752671532045_n.jpg?oh=03c554a42733f916ceed50ca741f2548&oe=5A9350AA" alt="Subramanyan Chandrasekhar">
        </div>
        <div class="caption-wrapper">
          <h3> The star cluster image shown below is taken from NASA's Chandra Observatory, named after Chandrasekhar. </h3>
        </div>
      </div>
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
  <div class="event-wrapper">
    <h1 style="color: #ffffff; margin: 0px; display: block; padding: 22px; font-size: 20pt; font-family: monospace; background-color: #222222;">
      Events
    </h1>
    <div class="black">
      <vue-event-calendar :events="events"></vue-event-calendar>
    </div>
  </div>
  <footer>
    <span>Copyright 2017</span>
  </footer>
  </div>
</template>


<script>
export default {
  data () {
    return {
      events: [{
        date: '2017/11/23', 
        title: 'Literary Rebellion',
        desc: 'In the photo exhibition Literary Rebellion, twelve Nobel Laureates in Literature are depcited in the Spanish photographer Kim Manresa’s gripping and beautiful images.',
      }, {
        date: '2017/11/29',
        title: 'Shifting Boundaries',
        desc: '',
      },{
        date: '2017/12/08',
        title: 'Nobel Prize Concert',
        desc: 'The internationally renowned conductor Gustavo Dudamel will be conducting the Royal Stockholm Philharmonic Orchestra at the 2017 Nobel Prize Concert.',
      }]
    }
  }
}
</script>


<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}

h3 {
  font-weight: normal;
  text-align: left;
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
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
  /* height: 100vh; */
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
  width: 90%;
}

.image-wrapper {
  padding: 100px 0;
  width: 50%;
  float: left;
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
  padding: 100px 0;

}

.black .title {
  color: black;
}

#myCarousel {
  height: 80vh;
}

footer {
  margin: 20vh 0 0 0;
  text-align: center;
}

footer span {
  color: white;
}
</style>

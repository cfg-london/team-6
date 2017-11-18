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

    <div class="item">
      <div class="container">
        <div class="image-wrapper">
          <img src="http://nobelcenter.se/wp-content/uploads/2017/10/nobelcenter_Water_night_webb-portrait.jpg" alt="nobel center">
        </div>
        <div class="caption-wrapper">
          <h1>Nobel Prize Center</h1>
        </div>
      </div>
    </div>

    <div class="item">
      <div class="container">
        <div class="image-wrapper">
          <img src="http://nobelcenter.se/wp-content/uploads/2017/10/nobelcenter_Water_night_webb-portrait.jpg" alt="nobel center">
        </div>
        <div class="caption-wrapper">
          <h1>Nobel Prize Center</h1>
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
    <!-- <div class="row">
      <div class="col image-wrapper">
        <img src="http://nobelcenter.se/wp-content/uploads/2017/10/nobelcenter_Water_night_webb-portrait.jpg" alt="nobel center">
      </div>
      <div class="col">
        <h1>Nobel Prize Center</h1>
      </div>
    </div> -->
    <div style="max-width:450px;">
<iframe width="100%" height="300"  src="https://www.nobelprize.org/mediaplayer/embed_front_vod_tb.html?id=2723" style="border:0;margin-bottom:0px; margin-bottom: 15px;" frameborder="0" scrolling="no"></iframe>
  </div>
  <div class="black">
      <vue-event-calendar :events="events"></vue-event-calendar>
  </div>
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
  width: 60%;
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
</style>

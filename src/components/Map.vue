<template>
  <div class="container">
    <div id="map-container" style="position: relative; width: 800px; height: 600px;"></div>
  </div>
</template>

<script>
export default {
  name: 'Search',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  },
  created: function() {
    let mapScript = document.createElement('script');
    mapScript.setAttribute('src', 'node_modules/datamaps/dist/datamaps.world.min.js');
    document.head.appendChild(mapScript);
  },
  mounted: function() {
    var bubble_map = new Datamap({
      element: document.getElementById("map-container"),
      geographyConfig: {
        popupOnHover: false,
        highlightOnHover: false
      },
      fills: {
        defaultFill: '#ABDDA4',
        USA: 'blue',
        RUS: 'red'
      }
    });
    bubble_map.bubbles([
      {
        name: 'Albert Einstein',
        radius: 12,
        centered: 'DEU',
        country: 'USA',
        yeild: 0,
        fillKey: 'USA',
        date: 'weiwu!!!',
        imageUrl: 'https://www.nobelprize.org/nobel_prizes/physics/laureates/1921/einstein.jpg'
      },
      {
        name: 'Marie Curie',
        radius: 12,
        centered: 'POL',
        fillKey: 'USA',
        imageUrl: 'https://www.nobelprize.org/nobel_prizes/physics/laureates/1903/marie-curie_postcard.jpg'
      },
      {
        name: 'Niels Bohr',
        radius: 12,
        fillKey: 'USA',
        centered: 'DNK',
        imageUrl: 'https://www.nobelprize.org/nobel_prizes/physics/laureates/1922/bohr_postcard.jpg'
      },{
        name: 'J. J. Thompson',
        radius: 12,
        yeild: 50000,
        fillKey: 'USA',
        centered: 'GBR',
        imageUrl: 'https://www.nobelprize.org/nobel_prizes/physics/laureates/1906/thomson_postcard.jpg'
      }
    ], {
      popupTemplate: function(geo, data) {
        return '<div class="hoverinfo">Name:' + data.name  
        + '<img src="' + data.imageUrl + '">' + '</div>';
      }
});    
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
  height: 100%;
}
</style>

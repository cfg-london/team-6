<template>
  <div class="container">
    <div class="card-panel">
      <div class="row">
        <div class="col s12 m5">
          <div class="card">
            <div class="card-image">
              <img src="https://www.nobelprize.org/nobel_prizes/physics/laureates/1921/einstein_postcard.jpg">
              <span class="card-title">Albert Einstein</span>
            </div>
          </div>
        </div>
        <div class="col s12 m7">
          <div class="card">
            <div class="card-content">
                <h2><strong>Albert Einstein</strong></h2>
        		<p><strong><span itemprop="Name"><span itemprop="givenName">Albert</span><span itemprop="familyName"> Einstein</span></span></strong>
				</p>
				<p><strong>Born:</strong> <span itemprop="birthDate">14 March 1879</span>, Ulm, Germany</p>
				<p><strong>Died:</strong> <span itemprop="deathDate">18 April 1955</span>, Princeton, NJ, USA</p>
						
						
				<p><strong>Affiliation at the time of the award:</strong> <span itemprop="affiliation">Kaiser-Wilhelm-Institut (now Max-Planck-Institut) für Physik, Berlin, Germany</span></p>
				<p><strong>Prize motivation:</strong> "for his services to Theoretical Physics, and especially for his discovery of the law of the photoelectric effect"</p>
						
			    <p><strong>Field:</strong> theoretical physics</p>
						
		                		
				<p><i>Albert Einstein received his Nobel Prize one year later, in 1922.</i></p>
				<p><strong>Prize share:</strong> 1/1</p>        
            </div>
          </div>

        </div>
        
        <div class="col s12 m12 center-align">
 
        </div>
        <div class="col s12 m12">
          <div class="card-panel teal" style="text-align: center;">
            <div class="col s12 m12 center-align">
              <h2 class="waves-effect waves-light btn-large centre">Subscribe</h2>
            </div>
          <a> to our newsletter and get to know our latest news about Nobel Prizes </a>
          </div>
      </div>
      </div>
      
      <div class="row more">
        <div class="col s12 m4">
          <div class="card">
            <div class="card-image">
              <img src="images/sample-1.jpg">
              <span class="card-title">Card Title </span>
            </div>
            <div class="card-content">
              <p><strong> Did you know ? </strong></p>
              <p>111 Nobel Prizes in Physics have been awarded between 1901-2017.</p>
              <p> 47 Physics Prizes have been given to one Laureate only. </p>
              <p> 2 women have been awarded the Physics Prize so far. </p>
            </div>
            <div class="card-action">
              <a href="#">Click to find out more fun facts</a>
            </div>
          </div>
        </div>
        <div class="col s12 m4">
          <div class="card">
            <div class="card-image">
              <img src="images/sample-1.jpg">
              <span class="card-title">Card Title</span>
            </div>
            <div class="card-content">
              <p>The Nobel Prize in Physics 2017 was divided, one half awarded to Rainer Weiss, the other half jointly to Barry C. Barish and Kip S. Thorne. "for decisive contributions to the LIGO detector and the observation of gravitational waves".</p>
            </div>
            <div class="card-action">
              <a href="#">Click to explore 2017 Nobel Prize in Physics</a>
            </div>
          </div>
        </div>
        <div class="col s12 m4">
          <div class="card">
            <div class="card-image">
              <img src="images/sample-1.jpg">
              <span class="card-title">Card Title</span>
            </div>
            <div class="card-content">
              <p><strong> Most Popular Physics Laureates </strong></p>
              <p>1.Albert Einstein</p>
              <p>2.Marie Curie</p>
              <p>3.Niels Bohr</p>
              <p> 4.James Chadwick </p>
              <p>5.J.J. Thomson</p>
            </div>
            <div class="card-action">
              <a href="#">Click to explore more about the most popular physics laureates</a>
            </div>
          </div>
        </div>
      </div>
      
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
  color: gold;
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

.white-text {
    text-align: center;
}

.landing {
  width: 100%;
  font-family: "Roboto Mono", monospace;
}

.card-panel {
    height: 50%;
}

.btn-large {
    color: white;
    background: gold;
}

.more {
  margin: 50px 0 0 0;
}

</style>

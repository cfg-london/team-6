<template>
  <div class="container">
    <div class="card">
      <div class="card-image">
        <img v-bind:src="imageUrl">
        <span class="card-title">{{laureateName}}</span>
      </div>
      <div class="card-content">
        <p>{{introduction}}</p>
      </div>
      <div class="card-action">
        <a v-bind:href="link">Click here for more informations</a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'album-block',
  props: ['laureate-name', 'image-url', 'introduction', 'link'],
  methods: {
  },
  computed: {
    url: function() {
    }
  },
  created: function(){
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
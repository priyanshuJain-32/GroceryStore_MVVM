<template>
  <div class="welcome-message">
    <h1>Welcome to Shop of Life.</h1>
    <p>
      Here we sell something special.
    </p>
    <h3>Get Started</h3>
      <p>Start by <router-link to="/signup">signing up</router-link> for a user account and enjoy.</p>
  </div>
</template>

<script>
export default {
  name: 'WelcomeMessage',
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
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
</style>

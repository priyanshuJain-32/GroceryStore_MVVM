<template>
  <div class="hello">
    <p>
    </p>
    <h3>Project Brief</h3>
      <p>Welcome to my first Javascript project build on MVVM architecture.</p>
    <h3>Tech Used</h3>
      <p>Vue CLI | VueX | Vue Router | Python | REST-API | SQLITE | Redis | Celery</p>
    <h3>Get Started</h3>
      <p>Start by <router-link to="/signup">signing up</router-link> for a user account and enjoy.</p>
      <p>Thank you for taking the time to view my work.</p>
    <h3>Inspirational Links</h3>
    <ul>
      <li><a href="https://www.youtube.com/@academind">Academind</a></li>
      <li><a href="https://www.youtube.com/watch?v=6avJHaC3C2U">Art of Code</a></li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
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

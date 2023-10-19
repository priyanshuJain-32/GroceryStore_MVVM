<template>
  <div class="logininput">
    <label for="username"><b>Username</b></label> | 
    <input type="text" placeholder="Enter Username" name="username" required>
    <br><br>
    <label for="password"><b>Password</b></label> | 
    <input type="password" placeholder="Enter Password" name="password" required>
    
  </div>
</template>

<script>
export default {
  name: 'LoginInput',
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

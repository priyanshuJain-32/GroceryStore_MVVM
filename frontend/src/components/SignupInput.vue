<template>
  <div class="signupinput">
    <label for="first_name"><b>First Name</b></label> | 
    <input type="text" placeholder="First Name" name="first_name" required>
    
    <br><br>
    <label for="last_name"><b>Last Name</b></label> | 
    <input type="text" placeholder="Last Name" name="last_name">
  </div>
</template>

<script>
export default {
  name: 'SignupInput',
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

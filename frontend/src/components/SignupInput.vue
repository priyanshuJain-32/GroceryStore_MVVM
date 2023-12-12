<template>
  <div class="signup-input">
    <h3>{{ params.role.charAt(0).toUpperCase() + params.role.slice(1) }} SignUp</h3>
    <br>
    <label for="first_name"><b>First Name</b></label> | 
    <input v-model="params.first_name" @keyup="submitSignup" type="text" placeholder="First Name" name="first_name" required>
    <br>
    <br>
    <label for="last_name"><b>Last Name</b></label> | 
    <input v-model="params.last_name" @keyup="submitSignup" type="text" placeholder="Last Name" name="last_name">
    
    <br><br>
    <label for="username"><b>Username</b></label> | 
    <input v-model="params.user_name" @keyup="submitSignup" type="text" placeholder="Enter Username" name="username" required>
    <br><br>
    <label for="email"><b>Email</b></label> | 
    <input v-model="params.email" @keyup="submitSignup" type="text" placeholder="Enter Email" name="email" required>
    <br><br>
    <label for="password"><b>Password</b></label> | 
    <input v-model="params.password" @keyup="submitSignup" type="password" placeholder="Enter Password" name="password" required>
    <br><br>
    <button type="button" @click="registerUser">Sign Up</button>
  </div>
</template>

<script>
import { mapGetters, mapActions, mapMutations } from 'vuex';

export default {
  name: 'SignupInput',
  computed: {
    ...mapGetters('auth',['params'])
  },
  methods: {
    submitSignup() {
      this.signup(this.params);
    },
    ...mapMutations('auth',['signup']),
    ...mapActions('auth',['registerUser'])
  }
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

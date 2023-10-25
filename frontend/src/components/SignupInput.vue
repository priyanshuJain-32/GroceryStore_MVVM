<template>
  <div class="signupinput">
    <h3>Fill details to Signup</h3>
    <br>

    <label for="first_name"><b>First Name</b></label> | 
    <input :value="first_name" type="text" placeholder="First Name" name="first_name" required>
    <br>
    <br>
    <label for="last_name"><b>Last Name</b></label> | 
    <input :value="last_name" type="text" placeholder="Last Name" name="last_name">
    <br><br>
    <label for="username"><b>Username</b></label> | 
    <input :value="username" type="text" placeholder="Enter Username" name="username" required>
    <br><br>
    <label for="password"><b>Password</b></label> | 
    <input :value="password" type="password" placeholder="Enter Password" name="password" required>
    <br><br>
    <button @click="signup">Sign Up</button>
  </div>
</template>

<script>
import { mapState, mapMutations } from 'vuex';

export default {
  name: 'SignupInput',
  computed: {
    ...mapState('auth', {
      first_name: state => state.first_name,
      last_name: state => state.last_name,
      username: state => state.username,
      password: state => state.password
    })
  },
  methods: {
    signup() {
      // console.log("Component"+document.getElementsByName('first_name')[0].value);
      const first_name = first_name.value;
      const last_name = document.getElementsByName('last_name')
      const username = document.getElementsByName('username')[0].value
      const password = document.getElementsByName('password')[0].value
      console.log(first_name)
      this.$store.commit('signup',first_name, last_name, username, password);
    },
    ...mapMutations({signup: 'auth/signup'})
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

<template>
  <div class="signupinput">
    <h3>Fill details to Signup</h3>
    <br>

    <label for="first_name"><b>First Name</b></label> | 
    <input v-model="formData.first_name" type="text" placeholder="First Name" name="first_name" required>
    <br>
    <br>
    <label for="last_name"><b>Last Name</b></label> | 
    <input v-model="formData.last_name" type="text" placeholder="Last Name" name="last_name">
    <br><br>
    <label for="username"><b>Username</b></label> | 
    <input v-model="formData.username" type="text" placeholder="Enter Username" name="username" required>
    <br><br>
    <label for="password"><b>Password</b></label> | 
    <input v-model="formData.password" type="password" placeholder="Enter Password" name="password" required>
    <br><br>
    <button type="button" @click="submitSignup">Sign Up</button>
  </div>
</template>

<script>
import { mapState, mapMutations } from 'vuex';

export default {
  name: 'SignupInput',
  data(){
    return {
      formData: {
        first_name: '',
        last_name: '',
        username: '',
        password: '',
      }
    }
  },
  computed: {
    ...mapState('auth',['first_name', 'last_name', 'username', 'password'])
  },
  methods: {
    submitSignup() {
      const data =  this.formData;
      this.signup(data);
    },
    ...mapMutations('auth',['signup'])
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

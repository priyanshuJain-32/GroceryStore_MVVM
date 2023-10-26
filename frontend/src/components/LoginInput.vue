<template>
  <div class="login-input">
    <h3>Fill details to Signup</h3>
    <br>
    <label for="username"><b>Username</b></label> | 
    <input v-model="params.user_name" type="text" placeholder="Enter Username" name="username" required>
    <br><br>
    <label for="password"><b>Password</b></label> | 
    <input v-model="params.password" @input="submitLogin" type="password" placeholder="Enter Password" name="password" required>
    <!-- <br><br>
    <button type="button" @click="submitLogin">Login</button> -->
  </div>
</template>

<script>
import { mapGetters, mapMutations } from 'vuex';

export default {
  name: 'LoginInput',
  
  computed: {
    ...mapGetters('auth',['params'])
  },

  methods: {
    submitLogin() {
      this.userLogin(this.params);
    },
    ...mapMutations('auth',['userLogin']),
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

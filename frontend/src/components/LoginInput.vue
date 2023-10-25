<template>
  <div class="logininput">
    <h3>Fill details to Signup</h3>
    <br>
    <label for="username"><b>Username</b></label> | 
    <input v-model="formData.username" type="text" placeholder="Enter Username" name="username" required>
    <br><br>
    <label for="password"><b>Password</b></label> | 
    <input v-model="formData.password" type="password" placeholder="Enter Password" name="password" required>
    <br><br>
    <button type="button" @click="submitLogin">Sign Up</button>
  </div>
</template>

<script>
import { mapState, mapMutations } from 'vuex';
export default {
  name: 'LoginInput',
  data(){
    return {
      formData: {
        username: '',
        password: '',
      }
    }
  },
  computed: {
    ...mapState('auth',['username', 'password'])
  },
  methods: {
    submitLogin() {
      const data =  this.formData;
      this.login(data);
    },
    ...mapMutations('auth',['login'])
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

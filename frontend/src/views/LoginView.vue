<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/Circular_game_of_life.png">
    <LoginInput/>
    <br><br>
    <button type="button" @click="login">Login</button>
  </div>
</template>

<script>
// @ is an alias to /src
import LoginInput from '@/components/LoginInput.vue'
import { mapMutations, mapActions } from 'vuex';

export default {
  name: 'SignUpView',
  components: {
    LoginInput
  },
  methods: {
    login() {
      this.userRole('user');
      this.loginUser();
    },
    ...mapMutations('auth',['userRole']),
    ...mapActions('auth',['loginUser'])
  }
}
</script>

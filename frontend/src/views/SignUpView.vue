<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/Circular_game_of_life.png">
    <SignupInput/>
    <br>
    <LoginInput/>
  </div>
</template>

<script>
// @ is an alias to /src
import LoginInput from '@/components/LoginInput.vue'
import SignupInput from '@/components/SignupInput.vue'

export default {
  name: 'SignUpView',
  components: {
    LoginInput,
    SignupInput
  }
}
</script>

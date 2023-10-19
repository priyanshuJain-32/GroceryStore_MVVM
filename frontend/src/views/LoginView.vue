<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/Circular_game_of_life.png">
    <LoginInput/>
  </div>
</template>

<script>
// @ is an alias to /src
import LoginInput from '@/components/LoginInput.vue'

export default {
  name: 'SignUpView',
  components: {
    LoginInput
  }
}
</script>

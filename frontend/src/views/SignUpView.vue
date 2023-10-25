<template>
  <div class="signup">
    <img alt="Vue logo" src="../assets/Circular_game_of_life.png">
    <SignupInput/>
  </div>
</template>

<script>
// @ is an alias to /src
import SignupInput from '@/components/SignupInput.vue'

export default {
  name: 'SignUpView',
  components: {
    SignupInput
  }
}
</script>

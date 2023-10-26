<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/Circular_game_of_life.png">
    <WelcomeMessage/>
  </div>
</template>

<script>
// @ is an alias to /src
import WelcomeMessage from '@/components/WelcomeMessage.vue'

export default {
  name: 'HomeView',
  components: {
    WelcomeMessage
  }
}
</script>
<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/Circular_game_of_life.png">
    <HelloWorld/>
    <h3>Developed by: {{ name }}</h3>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import { mapGetters } from 'vuex';

export default {
  name: 'HomeView',
  components: {
    HelloWorld
  },
  computed: {
    ...mapGetters('auth',{
      name: 'name'
    })
  }
}
</script>

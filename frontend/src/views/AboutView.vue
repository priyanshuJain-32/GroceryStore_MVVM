<template>
  <div class="about">
    <img alt="Vue logo" src="../assets/Circular_game_of_life.png">
    <HelloWorld/>
    <h3>Developed by: {{ creatorName }}</h3>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import { mapGetters } from 'vuex';

export default {
  name: 'AboutView',
  components: {
    HelloWorld
  },
  computed: {
    ...mapGetters('meta',{
      creatorName: 'creatorName'
    })
  }
}
</script>
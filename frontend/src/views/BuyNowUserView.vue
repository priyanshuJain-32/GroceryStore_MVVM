<template>
  <div class="products">
    <img alt="Vue logo" src="../assets/Circular_game_of_life.png">
    <BuyNow/>
  </div>
</template>

<script>

import BuyNow from '@/components/BuyNow.vue';

export default {
  name: 'BuyNowUserView',
  components: {
    BuyNow
  },
}
</script>

<template>
  <div class="cart">
    <img alt="Vue logo" src="../assets/Circular_game_of_life.png">
    <CartTable/>
  </div>
</template>

<script>

import CartTable from '@/components/CartTable.vue';

export default {
  name: 'CartUserView',
  components: {
    CartTable
  },
}
</script>

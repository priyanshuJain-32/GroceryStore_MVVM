<template>
  <div class="orders">
    <img alt="Vue logo" src="../assets/Circular_game_of_life.png">
    <OrdersTable/>
  </div>
</template>

<script>

import OrdersTable from '@/components/OrdersTable.vue';

export default {
  name: 'OrdersUserView',
  components: {
    OrdersTable
  },
}
</script>

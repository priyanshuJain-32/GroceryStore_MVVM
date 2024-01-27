<template>
  <div class="orders">
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

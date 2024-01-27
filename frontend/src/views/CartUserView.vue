<template>
  <div class="cart">
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

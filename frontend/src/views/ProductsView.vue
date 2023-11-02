<template>
  <div class="products">
    <img alt="Vue logo" src="../assets/Circular_game_of_life.png">
    <ProductsTable/>
  </div>
</template>

<script>
// @ is an alias to /src
import ProductsTable from '@/components/ProductsTable.vue';

export default {
  name: 'ProductsUserView',
  components: {
    ProductsTable
  },
}
</script>

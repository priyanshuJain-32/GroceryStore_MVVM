<template>
  <div class="products">
    <ProductsTable/>
  </div>
</template>

<script>
// @ is an alias to /src
import ProductsTable from '@/components/ProductsTable.vue';

export default {
  name: 'ProductsUserView',
  components: {
    ProductsTable,
  },
}
</script>

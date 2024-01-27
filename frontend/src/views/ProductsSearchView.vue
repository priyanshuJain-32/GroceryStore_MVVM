<template>
  <div class="products">
    <SearchTable/>
  </div>
</template>

<script>
// @ is an alias to /src
import SearchTable from '@/components/SearchTable.vue';

export default {
  name: 'ProductsUserView',
  components: {
    SearchTable,
  },
}
</script>

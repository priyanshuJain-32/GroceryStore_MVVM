<template>
  <div class="category">
    <CategoriesTable/>
  </div>
</template>

<script>
// @ is an alias to /src
import CategoriesTable from '@/components/CategoriesTable.vue';

export default {
  name: 'CategoriesUserView',
  components: {
    CategoriesTable
  },
}
</script>

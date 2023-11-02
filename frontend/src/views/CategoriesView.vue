<template>
  <div class="category">
    <img alt="Vue logo" src="../assets/Circular_game_of_life.png">
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

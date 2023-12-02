<template>
  <div class="editCategory">
    <img alt="Vue logo" src="../assets/Circular_game_of_life.png">
    <AddCategory/>
    <button type="button" @click="putCategory()">Add Category</button>
  </div>
</template>

<script>
// @ is an alias to /src
import AddCategory from '@/components/AddCategory.vue'
import { mapActions } from 'vuex';
export default {
  name: 'EditCategoryView',
  components: {
    AddProduct
  },
  methods: {
    ...mapActions('category',['putCategory'])
  },
}
</script>

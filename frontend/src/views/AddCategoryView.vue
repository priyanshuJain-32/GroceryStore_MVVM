<template>
  <div class="addCategory">
    <img alt="Vue logo" src="../assets/Circular_game_of_life.png">
    <AddCategory/>
    <button type="button" @click="postCategory()">Add Category</button>
  </div>
</template>

<script>
// @ is an alias to /src
import AddCategory from '@/components/AddCategory.vue'
import { mapActions } from 'vuex';
export default {
  name: 'AddCategoryView',
  components: {
    AddProduct
  },
  methods: {
    ...mapActions('category',['postCategory'])
  },
}
</script>

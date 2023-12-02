<template>
  <div class="addProduct">
    <img alt="Vue logo" src="../assets/Circular_game_of_life.png">
    <AddProduct/>
    <button type="button" @click="postProduct()">Add Product</button>
  </div>
</template>

<script>
// @ is an alias to /src
import AddProduct from '@/components/AddProduct.vue'
import { mapActions } from 'vuex';
export default {
  name: 'AddProductView',
  components: {
    AddProduct
  },
  methods: {
    ...mapActions('product',['postProduct'])
  },
}
</script>

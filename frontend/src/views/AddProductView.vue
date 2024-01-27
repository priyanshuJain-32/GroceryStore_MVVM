<template>
  <div class="addProduct">
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

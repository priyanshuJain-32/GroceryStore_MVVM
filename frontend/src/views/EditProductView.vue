<template>
  <div class="editProduct">
    <AddProduct/>
    <button type="button" @click="putProduct()">Update Product</button>
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
    ...mapActions('product',['putProduct'])
  }
}
</script>

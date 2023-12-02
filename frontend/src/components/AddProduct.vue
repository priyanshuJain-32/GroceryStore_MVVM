<template>
  <div class="add-product">
    <h3>Enter Product Details</h3>
    <br>
    <label for="product_category"><b>Product Category</b></label> |
    <select v-model="productToAdd.product_category_id" @click="updateProduct()" name="product_category" required>
        <option v-for="category in categories" :key="category.category_id" :value="category.category_id">
          {{ category.category_name }}
        </option>
    </select>
    
    <br><br>
    <label for="product_name"><b>Product Name</b></label> | 
    <input v-model="productToAdd.product_name" @input="updateProduct()" type="text" placeholder="Product Name" name="product_name" required>
    
    <br><br>
    <label for="product_desc"><b>Product Description</b></label> | 
    <input v-model="productToAdd.product_desc" @input="updateProduct()" type="text" placeholder="Product Desc" name="product_desc">
    
    <br><br>
    <label for="sell_price"><b>Selling Price</b></label> | 
    <input v-model="productToAdd.sell_price" @input="updateProduct()" type="number" placeholder="Selling Price" name="sell_price" required>
    
    <br><br>
    <label for="cost_price"><b>Cost Price</b></label> | 
    <input v-model="productToAdd.cost_price" @input="updateProduct()" type="number" placeholder="Cost Price" name="cost_price" required>

    <br><br>

    <label for="unit_of_measurement"><b>Unit of Measurement</b></label> |
    <select v-model="productToAdd.unit_of_measurement" @click="updateProduct()" name="unit_of_measurement" required>
      <option value="BX">Piece</option>
      <option value="PC">Gram</option>
      <option value="KG">Kilogram</option>
      <option value="LN">Length</option>
      <option value="UN">Unit</option>
      <option value="BTL">Bottle</option>
    </select>

    <br><br>
    <label for="discount"><b>Discount</b></label> | 
    <input v-model="productToAdd.cost_price" @input="updateProduct()" type="number" placeholder="Discount" name="discount" required>

    <br><br>
    <label for="product_quantity"><b>Product Quantity</b></label> | 
    <input v-model="productToAdd.product_quantity" @input="updateProduct()" type="number" placeholder="Product Quantity" name="product_quantity" required>
    
    <br><br>
    <label for="expiry_date"><b>Expiry Date</b></label> | 
    <input v-model="productToAdd.expiry_date" @input="updateProduct()" type="date" placeholder="Expiry Date" name="expiry_date" required>

    <br><br>
  </div>
</template>

<script>
import { mapGetters, mapMutations } from 'vuex';

export default {
  name: 'AddProduct',
  computed: {
    ...mapGetters('product',['productToAdd']),
    ...mapGetters('category',['categories']),
  },
  methods: {
    updateProduct(){
      this.updateEditProduct(this.productToAdd)
    },
    ...mapMutations('product',['updateEditProduct'])
  }
}
</script>

<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>

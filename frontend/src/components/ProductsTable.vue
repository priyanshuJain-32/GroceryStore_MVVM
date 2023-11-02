<template>
    <div class="products-table">

		<table id = "product-table" class="table" style="width: 95%; text-align: center;">
			<th>Category Id</th>
			<th>Category</th>
			<th>Product</th>
			<th>Product Desc</th>
			<th>Price/ Unit</th>
			<th v-if="params.role == 'manager' || params.role == 'admin'">Available Quantity</th>
			<th>Discount %</th>
			<th>Offer Price</th>
			<th>Product Expiry Date</th>
			<th></th>
			<th></th>
			
			<tr v-for="product in products.products" :key="product.product_id">
				<div v-if="product.quantity==0">Out of Stock</div>
					<td>{{ product.product_category_id }}</td>
					<td>{{ product.product_category }}</td>
					<td>{{ product.product_name }}</td>
					<td>{{ product.product_desc }}</td>
					<td>{{ product.sell_price }}</td>
					<td v-if="params.role == 'manager' || params.role=='admin'">{{ product.product_quantity }}</td>
					<td>{{ product.discount }}</td>
					<td>{{ (product.sell_price|int)*(100-product.discount)/100 }}</td>
					<td>{{ product.expiry_date }}</td>
					
					<td><router-link :to="'/buy-now-user-view/' + product.product_id">Buy Now</router-link></td>
					<td><form>
						<input type="button" @click="this.addToCart" style="width: 150px;" name="cart_product" value = "Add to Cart"/></form></td>
			</tr>
			<td></td>
			
		</table>
    </div>
</template>




<script>
import { mapGetters, mapActions } from 'vuex';

export default {
  name: 'ProductsTable',
  computed: {
    ...mapGetters('auth',['params']),
	...mapGetters('product',['products']),
	...mapGetters('category',['categories'])
  },
  methods: {
	...mapActions('product',['buyNow']),
	...mapActions('cart',['addToCart'])
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
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

<template>
    <div class="product-table">

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
			
			<tr>
				<td>{{ product.product_category_id }}</td>
				<td>{{ product.product_category }}</td>
				<td>{{ product.product_name }}</td>
				<td>{{ product.product_desc }}</td>
				<td>{{ product.sell_price }}</td>
				<td v-if="params.role == 'manager' || params.role=='admin'">{{ product.product_quantity }}</td>
				<td>{{ product.discount }}</td>
				<td>{{ (product.sell_price|int)*(100-product.discount)/100 }}</td>
				<td>{{ product.expiry_date }}</td>
				
				<td><form>
					<input type="submit" @click="buyComplete(product.product_id)" style="width: 120px;" name="buy_product" value = "Buy Now"/></form></td>
				<td><form>
					<input type="submit" @click="cartProduct(product.product_id)" style="width: 150px;" name="cart_product" value = "Add to Cart"/></form></td>
			</tr>
			<td></td>
			
		</table>
		<div v-if="product === undefined">Product not found</div>
    </div>
</template>


<script>
import { mapGetters, mapActions } from 'vuex';

export default {
  name: 'ProductsTable',
  computed: {
	
	product() {return this.productById(this.$route.params.product_id)},
	...mapGetters('auth',['params']),
	...mapGetters('product',['productById'])
	
  },
  methods: {
	...mapActions('product',['buyNow']),
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

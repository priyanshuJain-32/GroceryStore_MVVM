// Fix Cart data flow while carting products the current logic just adds items into cart and does not fix it.

<template>
    <div class="cart-table">

		<table id = "cart-table" class="table" style="width: 95%; text-align: center;">
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
			
			<tr v-for="product in fullOrders.products" :key="product.product_id">
				<div v-if="product.quantity==0">Out of Stock</div>
					<td>{{ product.product_category_id }}</td>
					<td>{{ product.product_category }}</td>
					<td>{{ product.product_name }}</td>
					<td>{{ product.product_desc }}</td>
					<td>{{ product.sell_price }}</td>
					<td v-if="params.role == 'manager' || params.role=='admin'">{{ product.product_quantity }}</td>
					<td>{{ product.discount }}</td>
					<td>{{ (parseInt(product.sell_price))*(100-product.discount)/100 }}</td>
					<td>{{ product.expiry_date }}</td>
					
					<td><router-link :to="'/buy-now-user-view/' + product.product_id">Buy Now</router-link></td>
					<td><form>
						<input type="button" @click="this.addToCart(product.product_id)" style="width: 150px;" name="cart_product" value = "Add to Cart"/></form></td>
					<td><form>	
						<input type="button" @click="this.decrementCart(product.product_id)" style="width: 150px;" name="reduce_cart_product" value = "Delete from Cart"/></form></td>
			</tr>
		</table>
		<form>
			<input type="button" @click="this.checkoutCart" style="width: 150px;" name="checkout_cart" value = "Checkout Cart"/>
		</form>
    </div>
</template>


<script>
import { mapGetters, mapActions } from 'vuex';

export default {
  name: 'ProductsTable',
  computed: {
    ...mapGetters('auth',['params']),
	...mapGetters('order',['fullOrders'])
  },
  methods: {
	...mapActions('order',['buyNow', 'fetchOrders']),
  },
  beforeMount(){
	this.fetchOrders()	
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

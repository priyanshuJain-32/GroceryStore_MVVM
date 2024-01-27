<template>
    <div class="cart-table">

		<table id = "cart-table" class="table" style="width: 95%; text-align: center;">
			<th>Category Id</th>
			<th>Category</th>
			<th>Product</th>
			<th>Product Desc</th>
			<th>Price/ Unit</th>
			<th>Discount %</th>
			<th>Offer Price</th>
			<th>Cart Quantity</th>
			<th>Total Value</th>
			<th>Product Expiry Date</th>
			<th></th>
			<th></th>
			
			<tr v-for="product in fullCart.products" :key="product.product_id">
				<div v-if="product.quantity==0">Out of Stock</div>
					<td>{{ product.product_category_id }}</td>
					<td>{{ product.product_category }}</td>
					<td>{{ product.product_name }}</td>
					<td>{{ product.product_desc }}</td>
					<td>{{ product.sell_price }}</td>
					<td>{{ product.discount }}</td>
					<td>{{ (parseInt(product.sell_price))*(100-product.discount)/100 }}</td>
					<td>{{ product.cart_quantity }}</td>
					<td>{{ (parseInt(product.sell_price))*(100-product.discount)/100*product.cart_quantity }}</td>
					<td v-if="(product.expiry_date!==null && product.expiry_date!=='')">{{ product.expiry_date }}</td>
					<td v-if="!(product.expiry_date!==null && product.expiry_date!=='')">NA</td>
					
					<td><router-link :to="'/buy-now-user-view/' + product.product_id">Buy Now</router-link></td>
					<td><form>
						<input type="button" @click="this.addToCart(product.product_id)" style="width: 150px;" name="cart_product" value = "Add More"/></form></td>
					<td><form>	
						<input v-if="product.cart_quantity != 0" type="button" @click="this.decrementCart(product.product_id)" style="width: 150px;" name="reduce_cart_product" value = "Reduce from Cart"/></form></td>
			</tr>
		</table>
		<h3>Total Cart Value: {{ fullCart.total_value }} </h3>
		<form>
			<input type="button" v-if="fullCart.total_value!=0" @click="this.checkoutCart" style="width: 150px;" name="checkout_cart" value = "Checkout Cart"/>
		</form>
    </div>
</template>

<script>
import { mapGetters, mapMutations, mapActions } from 'vuex';

export default {
  name: 'CartTable',

  // Import cart state
  computed: {
    // ...mapGetters('auth',['params']),
	...mapGetters('cart',['cart', 'fullCart'])
  },
  methods: {
	
	// Adds buyNow action to the button
	...mapActions('product',['buyNow']),

	// Adds increment and decrement cart mutations
	...mapMutations('cart',['addToCart','decrementCart']),
	
	// Adds actions to add stuff to cart at backend and checkoutCart
	...mapActions('cart',['cartProducts', 'checkoutCart'])

  },

  // Lifecycle hook to load cart before unmounting the app
  beforeUnmount(){
	this.cartProducts()	
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

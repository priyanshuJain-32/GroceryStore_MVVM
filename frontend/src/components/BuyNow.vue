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
			</tr>
		</table>
		
		<form v-if="product.product_quantity != 0">
			<label for="buy_product"><b>Enter Quantity</b></label> | 
			<input v-model="order.order_quantity" type="number" placeholder="Enter Quantity" name="order_quantity" max="5" min="1" required/>
			
			<input type="button" @click="completeBuy" style="width: 150px;" name="cart_product" value = "Buy"/>
		</form>
		
		<div v-if="product.product_quantity == 0">Out of Stock</div>
    </div>
</template>


<script>
import { mapGetters, mapMutations, mapActions } from 'vuex';

export default {
  name: 'ProductsTable',
  computed: {
	
	product() {return this.productById(this.$route.params.product_id)},
	...mapGetters('auth',['params']),
	...mapGetters('product',['productById']),
	...mapGetters('order',['order'])
	
  },
  methods: {
	completeBuy(){
		this.setQuantity(this.order)
		this.buyNow({product_id: this.$route.params.product_id,
		order_quantity: this.order.order_quantity})
	},
	...mapMutations('order',['setQuantity']),
	...mapActions('order',['buyNow']),
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

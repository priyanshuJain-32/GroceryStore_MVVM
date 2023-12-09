<template>
    <div class="order-table">

		<table id = "order-table" class="table" style="width: 95%; text-align: center;">
			<th>Order Id</th>
			<th>Order date</th>
			<th>Product Id</th>
			<th>Product Name</th>
			<th>Product Desc</th>
			<th>Product Price</th>
			<th>Discount %</th>
			<th>Order Quantity</th>
			<th>Paid Amount</th>
			
			<tr v-for="order in getOrders.orders" :key="order.order_id">
				<td>{{ order.order_id }}</td>
				<td>{{ order.sell_date }}</td>
				<td>{{ order.order_product_id }}</td>
				<td>{{ order.order_product_name }}</td>
				<td>{{ order.order_product_desc }}</td>
				<td>{{ order.order_sell_price }}</td>
				<td>{{ order.order_discount }}</td>
				<td>{{ order.order_quantity }}</td>
				<td>{{ (parseInt(order.order_sell_price))*(100-order.order_discount)/100*order.order_quantity }}</td>
				
			</tr>
		</table>
    </div>
</template>


<script>
import { mapGetters, mapActions } from 'vuex';

export default {
  name: 'ProductsTable',
  computed: {
	...mapGetters('order',['getOrders'])
  },
  methods: {
	...mapActions('order',['fetchOrders']),
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

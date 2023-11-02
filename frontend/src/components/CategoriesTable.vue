<template>
    <div class="products-table">

		<!-- <div v-for="category in categories" :key="category.category_id"> -->
			<table id = "product-table" class="table" style="width: 95%; text-align: center;">
				<th>Category Id</th>
				<th>Category Name</th>
				<th></th>
				<th></th>
				
				<tr v-for="category in categories" :key="category.category_id">
					<!-- <div v-if="product.product_id in category.category_product_id" > -->
						
						<td>{{ category.category_id }}</td>
						<td><router-link to="/products-user-view/{{ category.category_id }}">{{ category.category_name }}</router-link></td>
						<td><router-link to="/products-user-view/{{ category.category_id }}">{{ category.category_name }}</router-link></td>
						
						<!-- <td>{{ product.sell_price }}</td>
						<td v-if="params.role == 'manager' || params.role=='admin'">{{ product.product_quantity }}</td>
						<td>{{ product.discount }}</td>
						<td>{{ (product.sell_price|int)*(100-product.discount)/100 }}</td>
						<td>{{ product.expiry_date }}</td> -->
						
						<!-- <td><form>
							<input type="submit" @click="orderPage(product_id=product.product_id)" style="width: 120px;" name="order_product" value = "Buy Now"/></form></td>
						<td><form>
							<input type="submit" style="width: 150px;" name="cart_product" value = "Add to Cart"/></form></td> -->
					<!-- </div> -->
				</tr>
				<td></td>
				
			</table>
		
		<!-- </div> -->
    
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
	orderPage(product_id){
		this.buyNow(product_id);
	},
	...mapActions('product',['buyNow'])
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

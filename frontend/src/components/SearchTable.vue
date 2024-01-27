<template>
    <div class="search-table">

		<br><br>
		<label for="select_searchBy"><b>Search By</b></label> |
		<select v-model="searchByThis.select_search_by" @click="updateSearch()" name="select_searchBy" required>
		<option value="category">Category</option>
		<option value="product">Product</option>
		</select>

		<label for="search_by"><b>Search Name</b></label> | 
		<input v-model="searchByThis.search_by_this_query" @input="updateSearch()" type="text" placeholder="Enter to search" name="search_by" required>
		<br><br>
		<form>
			<input type="button" @click="search()" style="width: 150px;" name="search" value = "Search"/>
		</form>
		<br><br>

		<table id = "search-table" class="table" style="width: 95%; text-align: center;">
			<th>Category Id</th>
			<th>Category</th>
			<th>Product Id</th>
			<th>Product</th>
			<th>Product Desc</th>
			<th>Price/ Unit</th>
			<th v-if="params.role == 'manager' || params.role == 'admin'">Cost Price</th>
			<th v-if="params.role == 'manager' || params.role == 'admin'">Available Quantity</th>
			<th>Discount %</th>
			<th>Offer Price</th>
			<th>Product Expiry Date</th>
			<th></th>
			<th></th>
			
			<tr v-for="product in searchedProducts.products" :key="product.product_category_id">
				<div v-if="product.quantity==0">Out of Stock</div>
					<td>{{ product.product_category_id }}</td>
					<td>{{ product.product_category }}</td>
					<td>{{ product.product_id }}</td>
					<td>{{ product.product_name }}</td>
					<td>{{ product.product_desc }}</td>
					<td>{{ product.sell_price }}</td>
					<td v-if="params.role == 'manager' || params.role=='admin'">{{ product.cost_price }}</td>
					<td v-if="params.role == 'manager' || params.role=='admin'">{{ product.product_quantity }}</td>
					<td>{{ product.discount }}</td>
					<td>{{ (parseInt(product.sell_price))*(100-product.discount)/100 }}</td>
					<td>{{ product.expiry_date }}</td>
					
					<td v-if="params.role=='user'">
						<!-- <router-link :to="'/buy-now-user-view/' + product.product_id">Buy Now</router-link> -->
						<form>
							<input type="button" @click="buyPage(product.product_id)" style="width: 150px;" name="buyNow" value = "Buy Now"/>
						</form>
					</td>
					<td v-if="params.role=='user'">
						<form>
							<input type="button" @click="this.addToCart(product.product_id)" style="width: 150px;" name="cart_product" value = "Add to Cart"/>
						</form>
					</td>
					<td v-if="params.role == 'manager' || params.role == 'admin'">
						<form>
							<input type="button" @click="sendToEditPage(product.product_id)" style="width: 150px;" name="edit_product" value = "Edit Product Details"/>
						</form>
					</td>
					<td v-if="params.role == 'manager' || params.role == 'admin'">
						<router-link :to="'/delete-product-view/' + product.product_id">Delete Product</router-link>
					</td>
			</tr>
			<td></td>
			
		</table>
		<div v-if="params.role == 'manager' || params.role == 'admin'">
			<form>
				<input type="button" @click="sendToAddPage()" style="width: 150px;" name="add_product" value = "Add New Product"/>
			</form> 
		</div>
		
    </div>
</template>




<script>
import { mapGetters, mapMutations, mapActions } from 'vuex';
import router from '@/router';
export default {
  name: 'ProductsTable',
  computed: {
	// search(){
	// 	return this.searchBy(this.searchByThis)
	// },
    ...mapGetters('auth',['params']),
	...mapGetters('product',['products', 'productById', 'searchByThis', 'searchedProducts']),
	...mapGetters('cart',['cart'])
  },
  methods: {
	buyPage(product_id){
		router.push(`/buy-now-user-view/${product_id}`)
	},
	sendToEditPage(product_id){
		this.setEditProduct(product_id)
		router.push(`/edit-product-view/${product_id}`)
	},
	sendToAddPage(){
		this.clearProduct()
		router.push('/add-product-view')
	},
	updateSearch(){
		this.updateSearchBy(this.searchByThis)
		this.searchBy()
	},
	search(){
		this.searchBy()
	},
	...mapActions('product',['buyNow', 'searchBy']),
	...mapMutations('product',['setEditProduct', 'clearProduct', 'updateSearchBy']),
	...mapMutations('cart',['addToCart']),
	...mapActions('cart',['updateCart', 'fetchCart'])

  },
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

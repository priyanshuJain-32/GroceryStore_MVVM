<template>
    <div class="products-table">

<!-- 
        <table id = "product-table" class="table" style="width: 95%; text-align: center;">
			<th>Product</th>
			<th>Product Desc</th>
			<th>Price/ Unit</th>
			<th>Available Quantity</th>
			<th>Discount %</th>
			<th>Offer Price</th>
			<th>Product Expiry Date</th>
			<th></th>
			<th></th>
			
			{% for product in category.products %}
			<tr>
			<td>{{ product.product_name }}</td>
			<td>{{ product.product_desc }}</td>
			<td>{{ product.sell_price }}</td>
			<td>{{ product.product_quantity }}</td>
			<td>{{ product.discount }}</td>
			<td>{{ (product.sell_price|int)*(100-product.discount)/100 }}</td>
			<td>{{ product.expiry_date }}</td>
			{% if product.product_quantity!=0 %}
			<td><form action="/order_product/{{ product.product_id }}" method="GET">
				<input type="submit" style="width: 120px;" name="order_product" value = "Buy Now"/></form></td>
			<td><form action="/cart_product/{{ product.product_id }}" method="POST">
				<input type="submit" style="width: 150px;" name="cart_product" value = "Add to Cart"/></form></td>
			</tr>
			{% else %}
			<td>Out of Stock</td>
			{% endif %}
			{% endfor %} -->
    
    
    </div>
</template>




<script>
import { mapGetters, mapActions } from 'vuex';

export default {
  name: 'ProductsTable',
  computed: {
    ...mapGetters('auth',['params'])
  },
  methods: {
    submitSignup() {
      this.signup(this.params);
      this.registerUser();
    },
    ...mapActions('product',['registerUser'])
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

<template>
  <div class="delete-product-view">
    <h2 v-if="params.role == 'admin'"> Are you sure you want to delete the product and all its data</h2>
    <h2 v-if="params.role == 'manager'"> Are you sure you want to submit request to delete the product and all its data</h2>
    {{ theProduct.product_id }}
    {{ theProduct.product_name }}
    <div v-if="params.role == 'admin'">
			<form>
				<input type="button" @click="deleteProductNow()" style="width: 150px;" name="delete_product" value = "Delete Product"/>
			</form>
    
		</div>
    <div v-if="params.role == 'manager'">
			<form>
				<input type="button" @click="submitToRequestState()" style="width: 150px;" name="submit_delete_product_request" value = "Delete Product Request"/>
			</form>
    
		</div>
  </div>
</template>

<script>
import { mapActions, mapMutations, mapGetters } from 'vuex';

export default {
  name: 'DeleteProductView',
  computed: {
    theProduct(){
      return this.productById(this.$route.params.product_id)
    },
    ...mapGetters('product',['productById']),
    ...mapGetters('auth',['params'])
  },
  methods: {
    deleteProductNow(){
      this.deleteProduct(this.$route.params.product_id)
    },

    submitToRequestState(){
      const payload = {'request_type': `delete_product_${this.$route.params.product_id}`}
      this.submitRequest(payload)
      this.postRequest()
    },

    ...mapActions('product',['deleteProduct']),

    ...mapMutations('request',['submitRequest']),
    ...mapActions('request',['postRequest']),

  }
}

</script>

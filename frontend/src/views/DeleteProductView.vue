<template>
  <div class="logout">
    <img alt="Vue logo" src="../assets/Circular_game_of_life.png">
    <h2> Are you sure you want to delete the product and all its data</h2>
    
    <div v-if="params.role == 'manager' || params.role == 'admin'">
			<form>
				<input type="button" @click="deleteProductNow()" style="width: 150px;" name="delete_product" value = "Delete Product"/>
			</form> 
		</div>
  </div>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  name: 'LogoutView',
  methods: {
    deleteProductNow(){
      this.deleteProduct(this.$route.params.product_id)
    },
    ...mapActions('product',['deleteProduct'])
  }
}

</script>

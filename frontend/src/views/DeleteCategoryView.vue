<template>
  <div class="deleteCategory">
    <img alt="Vue logo" src="../assets/Circular_game_of_life.png">
    <h2 v-if="params.role == 'admin'"> Are you sure you want to delete the category and all its products</h2>
    <h2 v-if="params.role == 'manager'"> Are you sure you want to submit request for deleting the category and all its products</h2>
    <div v-if="params.role == 'admin'">
			<form>
				<input type="button" @click="deleteCategoryNow()" style="width: 150px;" name="delete_category" value = "Delete Category"/>
			</form>
		</div>
    <div v-if="params.role == 'manager'">
			<form>
				<input type="button" @click="deleteCategoryRequest()" style="width: 150px;" name="delete_category_request" value = "Submit Request"/>
			</form>
		</div>
  </div>
</template>

<script>
import { mapActions, mapMutations } from 'vuex';
import router from '@/router';
export default {
  name: 'LogoutView',
  methods: {
    deleteCategoryNow(){
      this.deleteCategory(router.$route.params.category_id)
    },
    deleteCategoryRequest(){
      const request = {request_type: `delete_category_${router.$route.params.category_id}`}
      this.submitRequest(request)
      this.postRequest()
    },
    ...mapActions('category',['deleteCategory']),
    ...mapMutations('request',['submitRequest']),
    ...mapActions('request',['postRequest']),
  }
}
</script>

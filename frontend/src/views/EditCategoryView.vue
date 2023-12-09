<template>
  <div class="editCategory">
    <img alt="Vue logo" src="../assets/Circular_game_of_life.png">
    <AddCategory/>
    <div v-if="params.role == 'admin'">
      
      <form>
				<input type="button" @click="putCategory()" style="width: 150px;" name="update_category" value = "Update Category"/>
			</form>
    </div>
    <div v-if="params.role == 'manager'">
			<form>
				<input type="button" @click="submitToRequestState()" style="width: 150px;" name="submit_update_category_request" value = "Update Category"/>
			</form>
		</div>
  </div>
</template>

<script>
// @ is an alias to /src
import AddCategory from '@/components/AddCategory.vue'
import { mapActions, mapMutations, mapGetters } from 'vuex';
export default {
  name: 'EditCategoryView',
  components: {
    AddCategory
  },
  computed:{
    ...mapGetters('category',['getCategory']),
    ...mapGetters('auth',['params'])
  },
  methods: {
    submitToRequestState(){
      const payload = {'request_type': `update_category_${this.getCategory.category_name}_${this.$route.params.category_id}`}
      this.submitRequest(payload)
      this.postRequest()
    },
    ...mapActions('category',['putCategory']),
    ...mapMutations('request',['submitRequest']),
    ...mapActions('request',['postRequest'])

  },
}
</script>

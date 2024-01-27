<template>
  <div class="addCategory">
    <AddCategory/>
    <div v-if="params.role == 'admin'">
			<form>
				<input type="button" @click="postCategory()" style="width: 150px;" name="add_category" value = "Add Category"/>
			</form>
		</div>
    <div v-if="params.role == 'manager'">
			<form>
				<input type="button" @click="submitAddCategoryRequest()" style="width: 150px;" name="submit_add_category_request" value = "Submit Request"/>
			</form>
		</div>
  </div>
</template>

<script>
// @ is an alias to /src
import AddCategory from '@/components/AddCategory.vue'
import { mapActions, mapGetters, mapMutations } from 'vuex';
export default {
  name: 'AddCategoryView',
  components: {
    AddCategory
  },
  computed: {
    ...mapGetters('category',['getCategory']),
    ...mapGetters('auth',['params'])
  },
  methods: {
    submitAddCategoryRequest(){
      const request = {'request_type': `add_category_${this.getCategory.category_name}`}
      this.submitRequest(request)
      this.postRequest()
    },
    ...mapActions('category',['postCategory']),
    ...mapMutations('request',['submitRequest']),
    ...mapActions('request',['postRequest'])
  },
}
</script>

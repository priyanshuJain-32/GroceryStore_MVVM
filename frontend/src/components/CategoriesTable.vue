<template>
    <div class="category-table">

			<table id = "category-table" class="table" style="width: 95%; text-align: center;">
				<th>Category Id</th>
				<th>Category Name</th>
				<th></th>
				<th></th>
				
				<tr v-for="category in categories" :key="category.category_id">
						
				<td>{{ category.category_id }}</td>
				<td>{{ category.category_name }}</td>
				<td v-if="params.role == 'admin' || params.role=='manager'">
					<form>
						<input type="button" @click="editCategory(category.category_id)" style="width: 150px;" name="edit_category" value = "Change Category Name"/>
					</form>
				</td>

				<td v-if="params.role == 'admin' || params.role=='manager'">
					<form>
						<router-link :to="'/delete-category-view/' + category.category_id">Delete Category</router-link>
					</form>					
				</td>
				</tr>
				
			</table>
			<br><br>
			<div v-if="params.role == 'manager' || params.role == 'admin'">
			<form>
				<input type="button" @click="sendToAddPage()" style="width: 150px;" name="add_category" value = "Add New Category"/>
			</form> 
		</div>
    
    </div>
</template>


<script>
import router from '@/router';
import { mapGetters, mapMutations } from 'vuex';

export default {
  name: 'CategoriesTable',
  computed: {
    ...mapGetters('auth',['params']),
	...mapGetters('category',['categories'])
  },
  methods: {
	editCategory(category_id){
		this.setEditCategory(category_id)
		router.push(`/edit-category-view/${category_id}`)
	},
	sendToAddPage(){
		this.clearCategory()
		router.push("/add-category-view")
	},
	...mapMutations('category',['setEditCategory','clearCategory']),
  },
  beforeMount() {
	this.$store.dispatch('category/fetchCategories')
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

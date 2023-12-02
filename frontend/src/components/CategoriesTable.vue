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
						<input type="button" @click="deleteCategory()" style="width: 150px;" name="delete_category" value = "Delete Category"/>
					</form>					
				</td>
				</tr>
				
			</table>
    
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
	...mapMutations('category',['setEditCategory'])
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

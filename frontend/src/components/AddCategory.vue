<template>
    <div class="add-category">
		<br><br>
		<label for="category_name"><b>Category Name</b></label> | 
		<input v-model="getCategory.category_name" @input="updateCategory()" type="text" placeholder="Category Name" name="category_name" required>

    

    
    </div>
</template>


<script>
import { mapGetters, mapMutations, mapActions } from 'vuex';

export default {
  name: 'AddCategory',
  computed: {
    ...mapGetters('auth',['params']),
	...mapGetters('category',['getCategory'])
  },
  methods: {
	updateCategory(){
		this.updateEditCategory(this.getCategory)
	},
	commitCategory(){
		this.putCategory()
	},
	...mapMutations('category',['updateEditCategory']),
	...mapActions('category', ['putCategory','sendRequest'])

  },
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

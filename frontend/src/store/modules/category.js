import axios from "axios";
import { tokenConfig } from "../../utils/config";
import baseUrl from "../../utils/baseUrl";
import router from "@/router";

const category = {namespaced: true,
    
    state: () => ({
      categories: [],
      category_id: -1,
      category_name: '',
    }),
    
    getters: {
      categories(state){
        return state.categories
      },
      getCategory(state){
        return {
          category_id: state.category_id,
          category_name: state.category_name,
        }
      },
      categoryById: (state) => (id) => {
        return state.categories.find(category => category.category_id == id);
      },
    },

    mutations: {
      setCategories(state, payload){
        state.categories = payload;
      },

      setEditCategory(state, category_id){
        const category = state.categories.find(category => category.category_id == category_id)
        state.category_id = category_id
        state.category_name = category.category_name
      },

      updateEditCategory(state, payload){
        state.category_name = payload.category_name
      },

      updateCategories(state, payload){
        const index = state.categories.findIndex(category => category.category_id == payload.category_id)
        state.categories[index] = payload
      },

      deleteCategories(state, payload){
        const index = state.categories.findIndex(category => category.category_id == payload.category_id)
        delete state.categories[index]
      },

      clearCategory(state){
        state.category_id = -1,
        state.category_name = ''
      }
    },

    actions: {
      async fetchCategories(context) {
        const path =  `${baseUrl}/get_all_category`;
        console.log("reached here in category")
        axios.get(path, tokenConfig(context.rootGetters['auth/token'].jwt))
        .then((response) => {
          context.commit('setCategories', response.data)
        }).catch(error => {
          console.error('fetchFailed', error)
        })
      },

      async postCategory(context){
        const path = `${baseUrl}/post_category`
        const payload = context.rootGetters['category/getCategory']
        axios.post(path, payload, tokenConfig(context.rootGetters['auth/token'].jwt))
        .then((response) => {
          context.commit('updateCategories', payload)
          console.log(response)
          router.push('/categories-staff-view')
        }).catch(error => {
          console.error('postFailed', error)
        })
      },

      async putCategory(context){
        const path = `${baseUrl}/put_category`
        const payload = context.rootGetters['category/getCategory']
        axios.put(path, payload, tokenConfig(context.rootGetters['auth/token'].jwt))
        .then((response) => {
          context.commit('updateCategories', payload)
          console.log(response)
          router.push('/categories-staff-view')
        }).catch(error => {
          console.error('putFailed', error)
        })
      },

      async deleteCategory(context, category_id){
        const path = `${baseUrl}/delete_category/${category_id}`
        axios.delete(path, tokenConfig(context.rootGetters['auth/token'].jwt))
        .then((response) => {
          console.log(response)
          context.dispatch('product/fetchProducts','',{root: true})
          router.push('/categories-staff-view')
        }).catch(error => {
          console.error('delete Failed', error)
        })
      }
    }
  }

export default category;
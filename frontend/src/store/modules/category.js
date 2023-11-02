import axios from "axios";
import { tokenConfig } from "./config";
import baseUrl from "./baseUrl";
// import { isValidJwt } from "../../utils/index";
import router from "@/router";

const category = {namespaced: true,
    
    state: () => ({
      categories: [],
    }),
    
    getters: {
      categories(state){
        return state.categories;
      }
    },

    mutations: {
      setCategories(state, payload){
        state.categories = payload;
      }
    },
    
    actions: {
      async fetchCategories(context) {
        const path =  `${baseUrl}/get_all_category`;
        console.log("reached here in category")
        axios.get(path, tokenConfig(context.rootGetters['auth/token'].jwt))
        .then((response) => {
          context.commit('setCategories', response.data)
          context.dispatch('product/fetchProducts','',{ root: true })
          router.push('/categories-user-view')
        }).catch(error => {
          console.error('fetchFailed', error)
        })
      },
    }
  }

  export default category;
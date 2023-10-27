import axios from "axios";
import { tokenConfig } from "./config";
import baseUrl from "./baseUrl";
import router from "@/router";

const product = {namespaced: true,
    
    state: () => ({
      products: [],
    }),
    
    getters: {
      products(state){
        return {
          products: state.products,
        }
      },
    },

    mutations: {
      setProducts(state, payload){
        state.products = payload
      }
    },
    
    actions: {
        async fetchProducts(context) {
          const path =  `${baseUrl}/fetch_products`;
          console.log("reached here in product")
          axios.get(path, tokenConfig(context.rootGetters['auth/token'].jwt))
          .then((response) => {
            context.commit('setProducts', response.data)
            router.push('/products-user-view')
          }).catch(error => {
            console.error('fetchFailed', error)
          })
        },
    }
  }

  export default product;
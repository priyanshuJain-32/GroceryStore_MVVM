import axios from "axios";
import { tokenConfig } from "../../utils/config";
import baseUrl from "../../utils/baseUrl";
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
      productById: (state) => (id) => {
        return state.products.find(product => product.product_id == id);
      }
      
    },

    mutations: {
      setProducts(state, payload){
        state.products = payload
      }
    },
    
    actions: {
        async fetchProducts(context) {
          const path = `${baseUrl}/get_all_product`;
          console.log("reached here in product")
          axios.get(path, tokenConfig(context.rootGetters['auth/token'].jwt))
          .then((response) => {
            context.commit('setProducts', response.data)
            router.push('/products-user-view')
          }).catch(error => {
            console.error('fetchFailed', error)
          })
        },
    },
  }

  export default product;
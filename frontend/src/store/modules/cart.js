


// ##################### REMOVE AFTER DONE #######################################

import axios from "axios";
import { tokenConfig } from "./config";
import baseUrl from "./baseUrl";

const cart = {namespaced: true,
    
    state: () => ({
      cart: [],
    }),
    
    getters: {
      cart(state){
        return {
          cart: state.cart,
        }
      },
    },

    mutations: {
      
    },
    
    actions: {
        async buyProducts(context) {
          const path =  `${baseUrl}/buy_products`;
          axios.post(path, tokenConfig(context.state.jwt))
          .then((response) => {
            // context.commit('setToken', response.data)
          }).catch(error => {
            console.error('failedAuthentication', error)
          })
        },

        async 
        
    }
  }

  export default cart;
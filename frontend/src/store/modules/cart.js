


// ##################### REMOVE AFTER DONE #######################################

import axios from "axios";
import { tokenConfig } from "./config";
import baseUrl from "./baseUrl";

const auth = {namespaced: true,
    
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
            context.commit('setToken', response.data)
          }).catch(error => {
            console.error('failedAuthentication', error)
          })
        },

        async loginUser(context){
          const path = `${baseUrl}/login`;
          const userData = {
            'user_name' : context.state.user_name,
            'password' : context.state.password,
            'role': context.state.role
          };
          axios.post(path, userData, config)
          .then((response) => {
            console.log(response)
            context.commit('setToken', response.data)
          }).catch(error => {
            console.error('failedAuthentication', error)
            throw "WRONG CREDENTIALS";
          })
        },
    }
  }

  export default cart;
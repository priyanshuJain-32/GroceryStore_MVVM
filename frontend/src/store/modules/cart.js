import axios from "axios";
import { tokenConfig } from "../../utils/config";
import baseUrl from "../../utils/baseUrl";

const cart = {namespaced: true,
    
    state: () => ({
      cart: {},
      change: false,
    }),
    
    getters: {
      cart(state){
        return {
          cart: state.cart
        }
      },
      fullCart(state, getters, rootState, rootGetters){
        let keys = Object.keys(state.cart);
        let products = rootGetters['product/products'].products;
        let total_value = 0;
        // let product_keys = Object.keys(rootGetters['product/products'].products);
        let data = {};
        for (let i=0; i<keys.length; i++){
          data[keys[i]] = products[i];
          total_value += products[i].cost_price*state.cart[keys[i]];
        }
        return {
          products: data,
          total_value,
        };
      },

    },

    mutations: {
      addToCart(state, payload){
        if (!(payload in state.cart)){
          state.cart[payload] = 1
        } else {
          state.cart[payload] += 1
        }
        state.change = true;

      },
      decrementCart(state, payload){
        state.cart[payload] -= 1;
        if (state.cart[payload] == 0){
          delete state.cart[payload];
        }
        state.change = true;
      },

      mergeCart(state, payload){
        state.cart = payload.cart_data;
      },

      updateChange(state){
        state.change = false;
      },

      resetTotal(state){
        state.total_value = 0;
      }
    },
    
    actions: {

        async fetchCart(context) {
          const path = `${baseUrl}/view_cart`;
          axios.get(path, tokenConfig(context.rootGetters['auth/token'].jwt))
          .then((response)=> {
            console.log(response.data);
            context.commit('mergeCart', response.data);
          })
          .catch(error => {
            console.error('failedCartfetch', error)
          })
        },

        async cartProducts(context) {
          const path = `${baseUrl}/cart_products`;
          const payload = context.state.cart;
          if (payload == {}) {
            console.log('Nothing to cartback');
          } else if (!context.state.change) {
            console.log('No change to cartback')
          } else {
            axios.put(path, payload, tokenConfig(context.rootGetters['auth/token'].jwt))
            .then((response) => {
              console.log(response.data);
              context.commit('updateChange');
            }).catch(error => {
              console.error('failedCartProducts', error);
            })
          }
        },

        async checkoutCart(context) {
          const path = `${baseUrl}/checkout_cart`;
          const payload = context.state.cart;
          if (Object.keys(payload).length == 0) {
            console.log('Nothing to checkout');
          } else {
            await context.dispatch('cartProducts');
            axios.get(path, tokenConfig(context.rootGetters['auth/token'].jwt))
            .then((response) => {
              context.commit('mergeCart', {'cart_data': {}});
              context.commit('resetTotal');
              context.dispatch('order/fetchOrders','',{ root: true })
              context.commit('order/setOrders', {}, { root : true})

              console.log(response.data);
            }).catch((error) => {
              console.error('failedCheckoutError', error);
            })
          }
        },
    }
  }

export default cart;
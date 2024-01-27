import axios from "axios";
import { tokenConfig } from "../../utils/config";
import baseUrl from "../../utils/baseUrl";
import router from "@/router";


const cart = {namespaced: true,
    
    state: () => ({
      cart: {},
      change: false,
    }),
    
    //==========================================================================
    //=============================== GETTERS ==================================
    //==========================================================================

    getters: {

      // Update cart with fetched cart
      cart(state){
        return {
          cart: state.cart
        }
      },

      // Send the entire cart with products data to component
      fullCart(state, getters, rootState, rootGetters){
        let keys = Object.keys(state.cart);
        let products = rootGetters['product/products'].products;
        let total_value = 0;
        // let product_keys = Object.keys(rootGetters['product/products'].products);
        let data = {};
        for (let i=0; i<keys.length; i++){
          let product = products.find(product => product.product_id == keys[i])
          data[keys[i]] = product;
          total_value += product.sell_price*((100-product.discount)/100)*state.cart[keys[i]];
          data[keys[i]].cart_quantity = state.cart[keys[i]]
        }
        return {
          products: data,
          total_value,
        };
      },

    },

    //==========================================================================
    //=============================== MUTATIONS ================================
    //==========================================================================

    mutations: {
      
      // Mutation to increase the quantity of product in cart
      addToCart(state, payload){
        if (!(payload in state.cart)){
          state.cart[payload] = 1
        } else {
          state.cart[payload] += 1
        }
        state.change = true;

      },

      // Mutation to decrement the quantity in cart
      decrementCart(state, payload){
        state.cart[payload] -= 1;
        state.change = true;
      },

      // Mutation to overwrite the cart data with the changes
      mergeCart(state, payload){
        state.cart = payload.cart_data;
      },

      // Mutation to mark that the cart has been changed
      updateChange(state){
        state.change = false;
      },

      // Used when user checks out the cart
      resetTotal(state){
        state.total_value = 0;
      },

      // Used when user logs out
      resetCartState(state){
        state.cart = {}
        state.total_value = 0;
      }

    },
    
    //==========================================================================
    //=============================== ACTIONS ==================================
    //==========================================================================

    actions: {

        // Call to fetch the cart info 
        async fetchCart(context) {
          const path = `${baseUrl}/view_cart`;

          // Get call to fetch cart
          axios.get(path, tokenConfig(context.rootGetters['auth/token'].jwt))
          .then((response)=> {
            console.log(response.data);

            // Update the state with cart data
            context.commit('mergeCart', response.data);
          })
          .catch(error => {
            console.error('failedCartfetch', error)
          })
        },

        // Call to update cart at the backend
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
          const payload = context.rootGetters['cart/cart'];
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
              router.push("/orders-user-view")
              console.log(response.data);
            }).catch((error) => {
              console.error('failedCheckoutError', error);
            })
          }
        },
    }
  }

export default cart;
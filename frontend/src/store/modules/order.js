import axios from "axios";
import { tokenConfig } from "../../utils/config";
import baseUrl from "../../utils/baseUrl";
import router from "@/router";

const order = {namespaced: true,
    
    state: () => ({
      orders: {},
      order_quantity : 0,
    }),
    
    getters: {
      order(state){
        return {
          order_quantity: state.order_quantity,
        }
      },
      getOrders(state) {
        return {
          orders: state.orders
        }
      },
      // fullOrders(state, getters, rootState, rootGetters){
      //   let keys = Object.keys(state.orders);
      //   let products = rootGetters['product/products'].products;
      //   // let product_keys = Object.keys(rootGetters['product/products'].products);
      //   let data = {};
      //   for (let i=0; i<keys.length; i++){
      //     data[keys[i]] = products[state.orders[keys[i]].object_product_id];
      //   }
      //   return {products: data};
      // },
    },

    mutations: {
      setQuantity(state, payload){
        state.order_quantity = payload.order_quantity
      },
      setOrders(state, payload){
        state.orders = payload
      },
      resetOrdersState(state){
        state.orders = {}
        state.order_quantity = 0
      }
    },

    actions: {
        async fetchOrders(context) {
          const path = `${baseUrl}/get_all_order`;
          console.log("reached here in fetchOrder")
          if (Object.keys(context.state.orders).length == 0){
            axios.get(path, tokenConfig(context.rootGetters['auth/token'].jwt))
            .then((response) => {
              console.log(response.data)
              context.commit('setOrders', response.data)
              router.push('/orders-user-view')
              // router.push('/products-user-view') // Fix this one and send user to orders-user-view after he finishes order
            }).catch(error => {
              console.error('fetchFailed', error)
            })
          } else {
            console.log('Orders already fetched')
          }
        },

      async buyNow(context, payload) {
        console.log("line 1 inside buyNow")
        const path = `${baseUrl}/order_product`;
        console.log("reached here in buyNow order")
        axios.post(path, payload, tokenConfig(context.rootGetters['auth/token'].jwt))
        .then((response) => {
          console.log(response.data)
          context.dispatch('fetchOrders');
        }).catch(error => {
          console.error('orderFailed', error)
        })
      },
    },
}

export default order;
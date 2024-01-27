import axios from "axios";
import { tokenConfig } from "../../utils/config";
import baseUrl from "../../utils/baseUrl";
import router from "@/router";

const product = {namespaced: true,
    
    state: () => ({
      products: [],
      product_id: -1,
      product_name: '',
      product_desc: '',
      sell_price: 0.0,
      cost_price: 0.0,
      unit_of_measurement: '',
      discount: 0.0,
      product_quantity: 0.0,
      expiry_date: '',
      product_category_id: -1,
      product_category: '',
      search_by_this_query: '',
      select_search_by: '',
      searched_products: [],
    }),
    
    getters: {
      products(state){
        return {
          products: state.products,
        }
      },
      productById: (state) => (id) => {
        return state.products.find(product => product.product_id == id);
      },
      productToAdd(state) {
        return {
          product_id: state.product_id,
          product_name: state.product_name,
          product_desc: state.product_desc,
          sell_price: state.sell_price,
          cost_price: state.cost_price,
          unit_of_measurement: state.unit_of_measurement,
          discount: state.discount,
          product_quantity: state.product_quantity,
          expiry_date: state.expiry_date,
          product_category_id: state.product_category_id,
          product_category: state.product_category,
        }
      },
      searchByThis(state){
        return {
          search_by_this_query : state.search_by_this_query,
          select_search_by : state.select_search_by,
        }
      },
      searchedProducts(state){
        return {
          products: state.searched_products
        }
      }
    },
    mutations: {
      setProducts(state, payload){
        state.products = payload
      },
      setEditProduct(state, id){
        const product = state.products.find(product => product.product_id == id);
        state.product_id = id
        state.product_name = product.product_name
        state.product_desc = product.product_desc
        state.sell_price = product.sell_price
        state.cost_price = product.cost_price
        state.unit_of_measurement = product.unit_of_measurement
        state.discount = product.discount
        state.product_quantity = product.product_quantity
        if (isNaN(product.expiry_date)){
          state.expiry_date = ''
        } else {
          state.expiry_date = product.expiry_date
        }
        state.product_category_id = product.product_category_id
        state.product_category = product.product_category
      },

      updateEditProduct(state, productToAdd){
        state.product_id = productToAdd.product_id
        state.product_name = productToAdd.product_name
        state.product_desc = productToAdd.product_desc
        state.sell_price = productToAdd.sell_price
        state.cost_price = productToAdd.cost_price
        state.unit_of_measurement = productToAdd.unit_of_measurement
        state.discount = productToAdd.discount
        state.product_quantity = productToAdd.product_quantity
        if (isNaN(productToAdd.expiry_date)){
          state.expiry_date = ''
        } else {
          state.expiry_date = productToAdd.expiry_date
        }
        state.product_category_id = productToAdd.product_category_id
        state.product_category = productToAdd.product_category
      },
      updateProduct(state, productToAdd){
        const index = state.products.findIndex(product => product.product_id == productToAdd.product_id);
        if (index !== -1) {
          state.products[index] = productToAdd
        }
      },

      clearProduct(state){
        state.product_name = ''
        state.product_desc = ''
        state.sell_price = 0.0
        state.cost_price = 0.0
        state.unit_of_measurement = ''
        state.discount = 0.0
        state.product_quantity = 0.0
        state.expiry_date = ''
        state.product_category_id = -1
        state.product_category = ''
      },

      deleteProductState(state, payload){
        const index = state.products.findIndex(product => product.product_id == payload);
        if (index !== -1) {
          delete state.products[index]
        }
      },

      updateSearchBy(state, payload){
        state.search_by_this_query = payload.search_by_this_query
        state.select_search_by = payload.select_search_by
      }, 

      resetProductState(state){
        state.products = []
        state.product_name = ''
        state.product_desc = ''
        state.sell_price = 0.0
        state.cost_price = 0.0
        state.unit_of_measurement = ''
        state.discount = 0.0
        state.product_quantity = 0.0
        state.expiry_date = ''
        state.product_category_id = -1
        state.product_category = ''
        state.search_by_this_query = ''
        state.select_search_by = ''
        state.searched_products = []
      }
    },

    actions: {
        async fetchProducts(context) {
          const path = `${baseUrl}/get_all_product`;
          console.log("reached here in product")
          axios.get(path, tokenConfig(context.rootGetters['auth/token'].jwt))
          .then((response) => {
            context.commit('setProducts', response.data)
          }).catch(error => {
            console.error('fetchFailed', error)
          })
        },

        async postProduct(context) {
          const path = `${baseUrl}/post_product`;
          console.log("reached here in post product")
          const productData = context.rootGetters['product/productToAdd']
          axios.post(path, productData, tokenConfig(context.rootGetters['auth/token'].jwt))
          .then((response) => {
            console.log(response.data)
            context.dispatch('fetchProducts')
            router.push('/products-staff-view')
          }).catch(error => {
            console.error('postProductFailed', error)
          })
        },

        async putProduct(context) {
          const path = `${baseUrl}/put_product`;
          console.log("reached here in put product")
          const productData = context.rootGetters['product/productToAdd']
          console.log(productData)
          axios.put(path, productData, tokenConfig(context.rootGetters['auth/token'].jwt))
          .then((response) => {
            console.log(response.data)
            context.commit('updateProduct', productData)
            router.push('/products-staff-view')
          }).catch(error => {
            console.error('postProductFailed', error)
          })
        },

        async deleteProduct(context, payload) {
          const path = `${baseUrl}/delete_product/${payload}`;
          console.log("reached here in delete product")
          axios.delete(path, tokenConfig(context.rootGetters['auth/token'].jwt))
          .then((response) => {
            console.log(response.data)
            context.dispatch('fetchProducts')
            context.commit('clearProduct')
            router.push('/products-staff-view')
          }).catch(error => {
            console.error('deleteProductFailed', error)
          })
        },
        searchBy(context) {
          console.log("190")
          if(context.state.select_search_by =='product'){
            console.log("192")
            const products = context.state.products.filter(product => product.product_name == context.state.search_by_this_query)
            context.state.searched_products = products
          } else if(context.state.select_search_by == 'category'){
            console.log("196")
            const products = context.state.products.filter(product => product.product_category == context.state.search_by_this_query)
            context.state.searched_products = products
            console.log(products)
          }
        },
    },
  }

export default product;
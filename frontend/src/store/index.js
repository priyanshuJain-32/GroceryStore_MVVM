import { createStore } from 'vuex'
import meta from './modules/meta.js'
import auth from './modules/auth.js'
import product from './modules/product.js'
import category from './modules/category.js'
import order from './modules/order.js'
import cart from './modules/cart.js'
import request from './modules/request.js'

const store = createStore({ modules: {
    meta,  
    auth,
    product,
    category,
    order,
    cart,
    request,
    
  } 
})

export default(store);
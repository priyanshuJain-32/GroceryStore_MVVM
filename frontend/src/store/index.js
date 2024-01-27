import { createStore } from 'vuex'
// import VuexPersister from 'vuex-persister'
import meta from './modules/meta.js'
import auth from './modules/auth.js'
import product from './modules/product.js'
import category from './modules/category.js'
import order from './modules/order.js'
import cart from './modules/cart.js'
import request from './modules/request.js'
import jobs from './modules/jobs.js'

// const vuexPersister = VuexPersister({
//     key: 'vuex',
//     storage: window.localStorage,
//   }
// )

const store = createStore({ modules: {
    meta,  
    auth,
    product,
    category,
    order,
    cart,
    request,
    jobs,
  }
})

export default(store);
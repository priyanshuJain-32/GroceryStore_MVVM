import { createStore } from 'vuex'
import auth from './modules/auth.js'
import meta from './modules/meta.js'
import product from './modules/product.js'
import location from './modules/location.js'

const store = createStore({ modules: {
    meta,  
    auth,
    product,
    location,
    
  } 
})

export default(store);
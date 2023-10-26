import { createStore } from 'vuex'
import auth from './modules/auth.js'
import meta from './modules/meta.js'

const store = createStore({ modules: {
    meta,  
    auth,
    
  } 
})

export default(store);
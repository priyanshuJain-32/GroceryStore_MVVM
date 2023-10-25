import { createStore } from 'vuex'
import auth from './auth.js'
const store = createStore({ modules: {
    'auth': auth,
    
  } 
})

// store.registerModule()

export default(store);
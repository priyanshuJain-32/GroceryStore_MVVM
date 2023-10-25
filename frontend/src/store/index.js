import { createStore } from 'vuex'

const store = createStore()

store.registerModule('auth', {namespaced: true,
  state: () => ({
    first_name: 'Priyanshu',
    last_name: 'Jain',
    username: '',
    password: ''
  }),
  getters: {
    name(state) {
      return state.first_name+"_"+state.last_name;
    }
  },
  mutations: {
    signup(state, first_name, last_name, username, password) {
      // console.log('Store'+first_name);
      state.first_name = first_name;
      state.last_name = last_name;
      state.username = username;
      state.password = password;
      console.log(state.first_name);
    }
  },
  actions: {

  }
})

export default(store);
const auth = {namespaced: true,
    
    state: () => ({
      first_name: '',
      last_name: '',
      username: '',
      password: '',
      creator_name: 'Priyanshu_Jain'
    }),
    
    getters: {
      name(state) {
        return state.creator_name;
      }
    },

    mutations: {
      signup(state, data) {
        state.first_name = data.first_name;
        state.last_name = data.last_name;
        state.username = data.username;
        state.password = data.password;
      },
      login(state, data) {
        state.username = data.username;
        state.password = data.password;
      }
    },
    
    actions: {
        
    }
  }

  export default auth;
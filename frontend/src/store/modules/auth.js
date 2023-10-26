const auth = {namespaced: true,
    
    state: () => ({
      first_name: '',
      last_name: '',
      username: '',
      password: '',
    }),
    
    getters: {
      params(state){
        return {
          first_name: state.first_name,
          last_name: state.last_name,
          username: state.username,
          password: state.password
        }
      }
    },

    mutations: {
      signup(state, params) {
        state.first_name = params.first_name;
        state.last_name = params.last_name;
        state.username = params.username;
        state.password = params.password;
      },
      login(state, params) {
        state.username = params.username;
        state.password = params.password;
      }
    },
    
    actions: {
        async signup() {
          // const { data } = await axios.get("http://127.0.0.1:5000/api/category");
          // this.categories = data;
          // console.log(this.categories);
        }
    }
  }

  export default auth;
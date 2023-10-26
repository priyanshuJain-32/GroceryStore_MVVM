import axios from "axios";

const auth = {namespaced: true,
    
    state: () => ({
      categories: {},
    }),
    
    getters: {
      categories(state){
        return state.categories;
      }
    },

    mutations: {
      // signup(state, params) {
      //   state.first_name = params.first_name;
      //   state.last_name = params.last_name;
      //   state.username = params.username;
      //   state.password = params.password;
      // },
      // login(state, params) {
      //   state.username = params.username;
      //   state.password = params.password;
      // }
    },
    
    actions: {
        async getCat() {
          const { data } = await axios.get("http://127.0.0.1:5000/api/category");
          this.categories = data;
          console.log(this.categories);
        }
    }
  }

  export default auth;
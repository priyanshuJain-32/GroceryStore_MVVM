import axios from "axios";
import config from "./config";
import baseUrl from "./baseUrl";

const auth = {namespaced: true,
    
    state: () => ({
      first_name: '',
      last_name: '',
      role: '',
      user_name: '',
      password: ''
      
    }),
    
    getters: {
      params(state){
        return {
          first_name: state.first_name,
          last_name: state.last_name,
          role: state.role,
          user_name: state.user_name,
          password: state.password
        }
      }
    },

    mutations: {
      signup(state, params) {
        state.first_name = params.first_name;
        state.last_name = params.last_name;
        state.role = params.role;
        state.user_name = params.user_name;
        state.password = params.password;
      },
      userLogin(state, params) {
        state.user_name = params.user_name;
        state.password = params.password;
        state.role = 'user';
      }
    },
    
    actions: {
        async registerUser(context) {
          const path =  `${baseUrl}/signup`;
          const userData = {
            'name': context.state.first_name+" "+context.state.last_name,
            'user_name':context.state.user_name, 
            'password': context.state.password,
            'role': context.state.role
          }
          const { data } = await axios.post(path, userData, config);
          
          console.log(data);
        },

        async loginUser(context){
          const path = `${baseUrl}/login`;
          const userData = {
            'user_name' : context.state.user_name,
            'password' : context.state.password
          }
          const { data } = await axios.post(path, userData, config);
          // if (data['authentication'] == true) {
          //   console.log(data);
          // }
          console.log(data);
        }
    }
  }

  export default auth;
import axios from "axios";
import { tokenConfig, config } from "./config";
import baseUrl from "./baseUrl";

const auth = {namespaced: true,
    
    state: () => ({
      first_name: '',
      last_name: '',
      role: '',
      user_name: '',
      password: '',
      jwt: ''
      
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
      },
      setToken(state, data){
        console.log('Inside setToken')
        state.jwt = data.jwt;
      },
      setRole(state, role) {
        state.role = role;
      }
    },
    
    actions: {
        async registerUser(context) {
          const path =  `${baseUrl}/signup`;
          const userData = {
            'name': context.state.first_name+"_"+context.state.last_name,
            'user_name':context.state.user_name,
            'password': context.state.password,
            'role': context.state.role
          }
          const { data } = await axios.post(path, userData, config);
          
          context.commit('setToken', data)
        },

        async loginUser(context){
          const path = `${baseUrl}/login`;
          const userData = {
            'user_name' : context.state.user_name,
            'password' : context.state.password
          }
          const { data } = await axios.post(path, userData, config);
          context.commit('setToken', data)
        },
        
        async logout(context){
          const path = `${baseUrl}/logout`;
          const userData = {
            'user_name' : context.state.user_name,
            'password' : context.state.password
          }
          const { data } = await axios.post(path, userData, tokenConfig);
          context.commit('setToken', data)
        }

    }
  }

  export default auth;
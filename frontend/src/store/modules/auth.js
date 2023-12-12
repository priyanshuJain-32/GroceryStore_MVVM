import axios from "axios";
import { config } from "../../utils/config";
import baseUrl from "../../utils/baseUrl";
import { isValidJwt } from "../../utils/index";
import router from "@/router";

const auth = {namespaced: true,
    
    state: () => ({
      first_name: '',
      last_name: '',
      role: 'user',
      user_name: '',
      email: '',
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
          email: state.email,
          password: state.password
        }
      },
      token(state){
        return {
          jwt: state.jwt
        }
      }
    },

    mutations: {
      signup(state, params) {
        state.first_name = params.first_name;
        state.last_name = params.last_name;
        state.role = params.role;
        state.user_name = params.user_name;
        state.email = params.email;
        state.password = params.password;
      },
      userLogin(state, params) {
        state.user_name = params.user_name;
        state.password = params.password;
      },
      setUserRole(state, role) {
        state.role = role;
      },
      setToken(state, payload){
        state.jwt = payload.token;
      },
      unsetUser(state){
        state.first_name = '';
        state.last_name = '';
        state.role = 'user';
        state.user_name = '';
        state.email = '';
        state.password = '';
        state.jwt = '';
      },
      isAuthenticated(state){
        return isValidJwt(state.jwt)
      }
    },
    
    actions: {
        async registerUser(context) {
          const path =  `${baseUrl}/signup`;
          const userData = {
            'name': context.state.first_name+"_"+context.state.last_name,
            'user_name':context.state.user_name,
            'email':context.state.email,
            'password': context.state.password,
            'role': context.state.role
          }
          axios.post(path, userData, config)
          .then((response) => {
            if (userData.role == 'manager'){
              router.push('/request-submitted-view')
            } else {
              context.commit('setToken', response.data)
              context.dispatch('product/fetchProducts','',{ root: true })
              context.dispatch('cart/fetchCart', '', { root: true })
            }
          }).catch(error => {
            console.error('failedAuthentication', error)
          })
        },

        async loginUser(context){
          const path = `${baseUrl}/login`;
          const userData = {
            'user_name' : context.state.user_name,
            'email': context.state.email,
            'password' : context.state.password,
            'role': context.state.role
          };
          axios.post(path, userData, config)
          .then((response) => {
            context.commit('setToken', response.data)
            context.dispatch('product/fetchProducts', '', { root: true })
            context.dispatch('category/fetchCategories', '', { root: true })
            if (context.state.role == 'user'){
              context.dispatch('cart/fetchCart', '', { root: true })
              router.push('/products-user-view')
            } else if(context.state.role == 'admin'){
              context.dispatch('request/fetchRequests', '', { root: true })
              router.push('/dashboard-staff-view')
            } else {
              context.dispatch('request/fetchRequest', '', { root: true})
              router.push('/dashboard-staff-view')
            }
          }).catch(error => {
            console.error('failedAuthentication', error)
            throw "WRONG CREDENTIALS";
          })
        },
        
        logout(context){
          context.commit('unsetUser');
        }

    }
  }

  export default auth;
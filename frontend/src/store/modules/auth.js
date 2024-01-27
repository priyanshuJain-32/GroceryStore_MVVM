import axios from "axios";
import { config } from "../../utils/config";
import baseUrl from "../../utils/baseUrl";
import { isValidJwt } from "../../utils/index";
import router from "@/router";

// Handles the authentication at front end

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
    
    //==========================================================================
    //=============================== GETTERS ==================================
    //==========================================================================

    getters: {
      
      // Used to send the state to components
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

      // Used to send the token to tokenConfig
      token(state){
        return {
          jwt: state.jwt
        }
      }
    },

    //==========================================================================
    //=============================== MUTATIONS ================================
    //==========================================================================

    mutations: {

      // Updates the working state variables
      // Used for making backend calls
      signup(state, params) {
        state.first_name = params.first_name;
        state.last_name = params.last_name;
        state.role = params.role;
        state.user_name = params.user_name;
        state.email = params.email;
        state.password = params.password;
      },

      // Update state when user logs in
      userLogin(state, params) {
        state.user_name = params.user_name;
        state.password = params.password;
      },

      // Set user role each time user selects Admin, manager or user role
      setUserRole(state, role) {
        state.role = role;
      },

      // Set token received from backend
      setToken(state, payload){
        state.jwt = payload.token;
      },

      // Unset user when the user select logout
      unsetUser(state){
        state.first_name = '';
        state.last_name = '';
        state.role = 'user';
        state.user_name = '';
        state.email = '';
        state.password = '';
        state.jwt = '';
      },

      // Checks whether user has a valid jwt token at frontend
      isAuthenticated(state){
        return isValidJwt(state.jwt)
      }
    },
    
    //==========================================================================
    //=============================== ACTIONS ==================================
    //==========================================================================

    actions: {

      // Signup action
        async registerUser(context) {
          const path =  `${baseUrl}/signup`; // Loads the path
          
          // Loads user data from state
          const userData = {
            'name': context.state.first_name+"_"+context.state.last_name,
            'user_name':context.state.user_name,
            'email':context.state.email,
            'password': context.state.password,
            'role': context.state.role
          }

          // Sends the api post call to backend
          axios.post(path, userData, config)
          .then((response) => {

            // As manager needs approval post Signup request sends user to the right page
            if (userData.role == 'manager'){
              router.push('/request-submitted-view')
            } else {
              context.commit('setToken', response.data)

              // If the user role signed up then login the user
              context.dispatch('loginUser')
            }
          }).catch(error => {
            console.error('failedAuthentication', error)
          })
        },

        // Login User action
        async loginUser(context){
          const path = `${baseUrl}/login`;
          const userData = {
            'user_name' : context.state.user_name,
            'email': context.state.email,
            'password' : context.state.password,
            'role': context.state.role
          };
          // Post call to backend server to login the user
          axios.post(path, userData, config)
          .then((response) => {
            
            // Set token received from backend as it will be used in subsequent calls
            context.commit('setToken', response.data)

            // Make call to fetchProducts 
            context.dispatch('product/fetchProducts', '', { root: true })

            // Make call to fetchCategories
            context.dispatch('category/fetchCategories', '', { root: true })
            
            // Check role and send user to the correct page accordingly
            if (context.state.role == 'user'){

              // Make call to fetchCart in case of user
              context.dispatch('cart/fetchCart', '', { root: true })
              router.push('/products-user-view')
            } else if(context.state.role == 'admin'){

              // Make call to fetchRequests in case of admin
              context.dispatch('request/fetchRequests', '', { root: true })
              router.push('/dashboard-staff-view')
            } else {

              // Make call to fetchRequest only for the particular manager
              context.dispatch('request/fetchRequest', '', { root: true})
              router.push('/dashboard-staff-view')
            }
          }).catch(error => {
            console.error('failedAuthentication', error)
            throw "WRONG CREDENTIALS";
          })
        },
        
        // Unset the entire state in case of logout
        logout(context){
          if (context.state.role == 'user'){
            context.dispatch('cart/cartProducts', '', { root : true })
          }
          context.commit('unsetUser');
          context.commit('cart/resetCartState','', { root : true })
          context.commit('category/resetCategoryState','', { root : true })
          context.commit('jobs/resetJobsState', '', { root : true })
          context.commit('order/resetOrdersState', '', { root : true })
          context.commit('product/resetProductState', '', { root : true })
          context.commit('request/resetRequestState', '', { root : true })
        }
    }
  }

  export default auth;
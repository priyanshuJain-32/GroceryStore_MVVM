import axios from "axios";
import { tokenConfig } from "../../utils/config";
import baseUrl from "../../utils/baseUrl";
import router from "@/router";

const request = {namespaced: true,
    
    state: () => ({
      requests: [],
      request_id: -1,
      request_status: 'pending',
      request_type: '',
      requester_id: -1,
    }),
    
    getters: {
      requests(state){
        return {
          requests: state.requests,
        }
      },
      requestToChange(state){
        return{
          request_id: state.request_id,
          request_status: state.request_status,
          request_type: state.request_type,
          requester_id: state.requester_id,
        }
      },
      getSubmitRequest(state){
        return {request_type: state.request_type}
      }
    },

    mutations: {
      setRequests(state, payload){
        state.requests = payload;
      },
      // Will be used in store manager dashboard to submit new request
      submitRequest(state, payload){
        state.request_type = payload.request_type
      },

      deleteRequestState(state, payload){
        const thekey = state.requests.findIndex(request => request.request_id == payload.request_id);
        delete state.requests[thekey]
      },
      alterRequestState(state, payload){
        state.request_id = payload.request_id
        state.request_type = payload.request_type
        state.requester_id = payload.requester_id
      },
      alterRequestStatus(state, status){
        state.request_status = status
      },
      updateRequestState(state, payload){
        const index = state.requests.findIndex(request => request.request_id == payload.request_id);
        state.requests[index] = payload
      },
      resetRequestState(state){
        state.requests = []
        state.request_id = -1
        state.request_status = 'pending'
        state.request_type = ''
        state.requester_id = -1
      }
    },
    
    actions: {
      async fetchRequests(context){
        const path = `${baseUrl}/get_all_request`;
        axios.get(path, tokenConfig(context.rootGetters['auth/token'].jwt))
        .then((response) => {
          context.commit('setRequests', response.data)
        }).catch(error => {
          console.error('failedFetchRequests', error)
          throw "WRONG CREDENTIALS";
        })
      },

      async fetchRequest(context){
        const path = `${baseUrl}/get_request`;
        axios.get(path, tokenConfig(context.rootGetters['auth/token'].jwt))
        .then((response) => {
          context.commit('setRequests', response.data)
          router.push('/dashboard-staff-view')
        }).catch(error => {
          console.error('failedFetchRequests', error)
          throw "WRONG CREDENTIALS";
        })
      },

      async postRequest(context){
        const path = `${baseUrl}/submit_request`;
        const payload = context.rootGetters['request/getSubmitRequest']
        axios.post(path, payload, tokenConfig(context.rootGetters['auth/token'].jwt))
        .then(response => {
          context.dispatch('fetchRequest')
          console.log(response)
        }).catch(error => {
          console.error('submission failed', error)
          throw "Wrong request submission"
        })
      },
      async deleteRequest(context, payload){
        const path = `${baseUrl}/delete_request/${payload.request_id}`
        axios.delete(path, tokenConfig(context.rootGetters['auth/token'].jwt))
        .then(response => {
          console.log(response)
          context.dispatch('fetchRequests')
        }).catch(error => {
          console.error('delete failed', error)
          throw "Wrong request delete"
        })
      },
      async putRequest(context){
        const path = `${baseUrl}/alter_request_status`
        const payload = context.rootGetters['request/requestToChange']
        axios.put(path, payload, tokenConfig(context.rootGetters['auth/token'].jwt))
        .then(response => {
          console.log(response)
          context.commit('updateRequestState', payload)
          context.dispatch('category/fetchCategories', '', { root : true })
          context.dispatch('product/fetchProducts', '', { root : true })
        }).catch(error => {
          console.error('delete failed', error)
          throw "Wrong request delete"
        })
      }
    }
  }

export default request;
import axios from "axios";
import { tokenConfig } from "../../utils/config";
import baseUrl from "../../utils/baseUrl";

const cart = {namespaced: true,
    
    state: () => ({
      task_id: ''
    }),
    
    getters: {
      taskId(state){
        return {
          task_id: state.task_id
        }
      },
    },

    mutations: {
      setTaskId(state, payload){
        state.task_id = payload.task_id
      },
      unsetTaskId(state){
        state.task_id = ''
      },
      resetJobsState(state){
        state.task_id = ''
      }
    },
    
    actions: {
        async generateCsv(context, payload) {
          const path = `${baseUrl}/generate_csv/`+payload;
          axios.get(path, tokenConfig(context.rootGetters['auth/token'].jwt))
          .then((response)=> {
            console.log(response.data);
            context.commit('setTaskId', response.data);
            const task_id = context.rootGetters['jobs/taskId'].task_id;
            context.dispatch('getCsv', {"task_id": task_id, "payload": payload})
          })
          .catch(error => {
            console.error('failed generate csv', error)
          })
        },
        async getCsv(context, payload){
          const path = `${baseUrl}/get_csv/` + payload.task_id +"/"+ payload.payload;
          axios.get(path, tokenConfig(context.rootGetters['auth/token'].jwt, {responseType: 'blob'}))
          .then((response)=> {
            const blob = new Blob([response.data], { type: 'text/csv' });

            const link = document.createElement('a');
            link.href = window.URL.createObjectURL(blob);

            let currentDate = new Date().toJSON().slice(0, 19);
            link.download = `${payload.payload}_data_${currentDate}.csv`;

            document.body.appendChild(link);
            link.click();

            document.body.removeChild(link);
            window.URL.revokeObjectURL(link.href);
            
            console.log(response.data);
            context.commit('unsetTaskId');
          })
          .catch(error => {
            console.error('failed export', error)
          }) 
        }
    }
  }

export default cart;
// DELETE IF UNUSED


const location = {namespaced: true,
    
    state: () => ({
      location: '',
    }),
    
    getters: {
      getLocation(state){
        return {
          location: state.location,
        }
      },
    },

    mutations: {
      setLocation(state, payload){
        state.location = payload
      }
    },
    
    actions: {

    }
  }

  export default location;
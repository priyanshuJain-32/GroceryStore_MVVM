// Tested Ok

const meta = {namespaced: true,
    
    state: () => ({
      creator_name: 'Priyanshu_Jain',
      github: 'https://github.com/priyanshuJain-32'
    }),
    
    getters: {
      getMeta(state) {
        return {
          creator_name: state.creator_name,
          github: state.github
      }
    }
  }
}

export default meta;
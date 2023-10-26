// Tested Ok

const meta = {namespaced: true,
    
    state: () => ({
      creator_name: 'Priyanshu_Jain',
    }),
    
    getters: {
      creatorName(state) {
        return state.creator_name;
      },
    }
}

export default meta;
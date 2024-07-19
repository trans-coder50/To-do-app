import { createStore } from 'vuex'

export default createStore({
  state: {
    authInfo:{},
    authTokens : null,
   
    
  },
  getters: {
  },
  mutations: {
   
  },

  actions: {
  },
  modules: {
  }
})

/*
updated(){
     const data = {user_id:this.info.user_id}
      axios.post('http://127.0.0.1:8000/posts/',data)
          .then(response => {
            this.data=response.data
          })
          .catch((error)=>{
             console.log(error)})
  },
*/

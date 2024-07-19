<template>
    <div class="container">
          <div class="ulDiv">
              <ul>
                  <li v-for="(i,index) in data" :key="i.id" :id="i.id">
                     <h3  >{{index+1}} - {{i.post}}</h3>
                     <div>
                        <button @click="show=true,postId=i.id" >
                            <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" fill="#FAE69E" class="bi bi-pencil-square" viewBox="0 0 16 16">
  <path d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"/>
  <path fill-rule="evenodd" d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5v11z"/>
</svg>
                            </button><br>
                        <button @click="delConf=true,postDelId=i.id">
                            <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" fill="#FAE69E" class="bi bi-trash3-fill" viewBox="0 0 16 16">
  <path d="M11 1.5v1h3.5a.5.5 0 0 1 0 1h-.538l-.853 10.66A2 2 0 0 1 11.115 16h-6.23a2 2 0 0 1-1.994-1.84L2.038 3.5H1.5a.5.5 0 0 1 0-1H5v-1A1.5 1.5 0 0 1 6.5 0h3A1.5 1.5 0 0 1 11 1.5Zm-5 0v1h4v-1a.5.5 0 0 0-.5-.5h-3a.5.5 0 0 0-.5.5ZM4.5 5.029l.5 8.5a.5.5 0 1 0 .998-.06l-.5-8.5a.5.5 0 1 0-.998.06Zm6.53-.528a.5.5 0 0 0-.528.47l-.5 8.5a.5.5 0 0 0 .998.058l.5-8.5a.5.5 0 0 0-.47-.528ZM8 4.5a.5.5 0 0 0-.5.5v8.5a.5.5 0 0 0 1 0V5a.5.5 0 0 0-.5-.5Z"/>
</svg>
                        </button>
                     </div>
                  </li>
                  
              </ul>
          </div>
  
          
          <form method="post" @submit.prevent="sendData"  class="inputDiv"  >
          <input type="text" name="" id="" v-model="fill">
          <button type="submit">
            <svg xmlns="http://www.w3.org/2000/svg" width="36" height="36" fill="#FAE69E" class="bi bi-send-fill" viewBox="0 0 16 16">
  <path d="M15.964.686a.5.5 0 0 0-.65-.65L.767 5.855H.766l-.452.18a.5.5 0 0 0-.082.887l.41.26.001.002 4.995 3.178 3.178 4.995.002.002.26.41a.5.5 0 0 0 .886-.083l6-15Zm-1.833 1.89L6.637 10.07l-.215-.338a.5.5 0 0 0-.154-.154l-.338-.215 7.494-7.494 1.178-.471-.47 1.178Z"/>
</svg>
          </button>
     
          </form>
            <div class="updateDiv" v-if="show" >
                <div>
                    <button @click='show=false' class="upclose">close</button>
                </div>
                <form method="post" @submit.prevent="updatePost(), up = '' ,show=false">
                    <input type="text" v-model="up"><br>
                    <button type="submit">Update</button>
                </form>

            </div>

            <div class="updateDiv" v-if="delConf" >
                <div>
                    <h3>are you sure you want to delete this post?</h3><br>
                    <button @click='delConf=false'  class="upclose">close</button>
                </div>
                
                <form method="post" @submit.prevent="deletePost() ,delConf=false">
                    <button type="submit">Delete</button>
                </form>

            </div>
    </div>
  </template>
  
  <script>
  
  import jwt_decode from "jwt-decode"
  import axios from 'axios'
  export default {
  name:'container',
  data(){
      return{
          fill:'',
          info:'',
          data:'',
          show:false,
          postId:0,
          postDelId:0,
          delConf:false,
          up:'',
         
      }
  },
  created(){
      let x= localStorage.getItem('authTokens')
      let b =JSON.parse(x)
      this.info = jwt_decode(b.access)  
      
  },
  mounted(){
      const data = {user_id:this.info.user_id}
      axios.post('http://127.0.0.1:8000/posts/',data)
          .then(response => {
            this.data=response.data
          })
          .catch((error)=>{
             console.log(error)})
  },
  
  methods:{
  
    
   sendData(){
         
       const data={
      
          post:this.fill,
          user_id:this.info.user_id,
         
          
       }
       axios.post('http://127.0.0.1:8000/create/', data)
          .then(response => {
            const data = {user_id:this.info.user_id}
          axios.post('http://127.0.0.1:8000/posts/',data)
          .then(response => {
            this.data=response.data
          })
          .catch((error)=>{
             console.log(error)})
          })
          .catch((error)=>{
             console.log(error)})

         this.fill =''
         
      },
     
      updatePost(){
        const data = {post:this.up}
        const pk = this.postId
        console.log(pk)
                axios.post(`http://127.0.0.1:8000/update/${pk}/`, data)  
                .then(response =>{
                  const data = {user_id:this.info.user_id}
          axios.post('http://127.0.0.1:8000/posts/',data)
          .then(response => {
            this.data=response.data
          })
          .catch((error)=>{
             console.log(error)})
  
            } )
         
       
      },
       deletePost(){
        const ck = this.postDelId
        
                axios.delete(`http://127.0.0.1:8000/delete/${ck}/`)  
                .then(response =>{
                
                const data = {user_id:this.info.user_id}
          axios.post('http://127.0.0.1:8000/posts/',data)
          .then(response => {
            this.data=response.data
          })
          .catch((error)=>{
             console.log(error)})
               
            })
            
        
        
         
      },
      
  
  }
  }
  </script>
  
  <style>
  .container{
      width:600px;
      height:100vh;
      margin:0;
      padding-top:10px;
      display:flex;
      flex-direction:column;
      background: #2B2A31;
      position :relative
  }
    .ulDiv::-webkit-scrollbar{width:8px;}
  .ulDiv::-webkit-scrollbar-thumb{
     background-color: #FAE69E;
     width:8px;
     border-radius: 4px;
      
  }
  .ulDiv::-webkit-scrollbar-track{
     background-color: #40414F;
     
     
      
  }
  
  
  .inputDiv{
      width:580px;
      height:80px;
      margin:10px;
      display:flex;
      flex-direction:row;
      justify-content: center;
      align-items: center;
      position:absolute;
      bottom:0
     
  }
  .inputDiv button{
    
    border:none;

    background: none;

  }
  .inputDiv input{
      width:100%;
      height:40px;
      border:none;
      border-radius:10px;
      margin-right: 10px;
      background:#40414F;
     color:rgb(226, 221, 221);
    
  }
  .ulDiv{
      width: 600px;
      
      height:85%;
  display:flex;
  flex-direction:columen;
  align-items:flex-start;

  overflow-y: scroll;
      overflow-x:hidden;
  }
    .ulDiv button{
        border: none;
        background:none;
    }
  .ulDiv ul{
    width:100%
  }
  .ulDiv li{
      width:530px;
      list-style: none;
      padding:10px;
      margin:3px;
      border-radius:5px;
      background-color: #40414F;
      text-align: left;
      display:flex;
      justify-content: space-between;
      align-items: center;
      color:rgb(226, 221, 221);
      position:relative;
      right:20px
  }
   
  .updateDiv{
    background-color: #2B2A31;
;
    width: 400px;
    height:350px;
    position:absolute;
    top:50%;
    left:50%;
    transform:translate(-50%,-50%);
    display:flex;
    flex-direction:column;
    justify-content: center;
    align-items: center;
    border-radius:10px
  }
  .updateDiv input{
    
    width:350px;
    height:30px;
    border-radius: 5px;
    
      color:rgb(226, 221, 221);

   
      border:none;
     
      margin-bottom:10px;
      background:#40414F
    
  }
   .updateDiv h3{
    color:rgb(226, 221, 221);

   }

.upclose{
    position:absolute;
    top:10px;
    right:10px;
    color:#2B2A31;
    background: #FAE69E;
    border:none;
    width:60px;
    height:30px;
    border-radius:5px;
    font-size:18px;
    font-weight:normal;
}
button{
    cursor: pointer;
}
.updateDiv form button{
    color:#2B2A31;
    background: #FAE69E;
    border:none;
    width:80px;
    height:30px;
    border-radius:5px;
    font-size:18px;
    font-weight:normal;
}
@media screen and (max-width:840px){
    .container{
      width:500px;
  }
  .inputDiv{
      width:480px;
}
.ulDiv{
      width: 500px;
  }
  .ulDiv li{
      width:430px;
      
  }
}
@media screen and (max-width:720px){
    .container{
      width:400px;
  }
  .inputDiv{
      width:380px;
}
.ulDiv{
      width: 400px;
  }
  .ulDiv li{
      width:330px;
      
  }
  .updateDiv{
    width: 350px;
    height:320px;
   
  }
  .updateDiv input{
    
    width:300px;
    height:30px;
   
    
  }
}
@media screen and (max-width:630px){
    .container{
      width:360px;
  }
  .inputDiv{
      width:340px;
}
.ulDiv{
      width: 360px;
      justify-content: center;
  }
  .ulDiv li{
      width:300px;
      font-size: 16px ;
      
     
      
      
  }
  .updateDiv{
    width: 330px;
    height:300px;
   
  }
  .updateDiv input{
    
    width:300px;
    height:30px;
   
    
  }
  @media screen and (max-width:470px){
    .container{
      width:320px;
  }
  .inputDiv{
      width:300px;
}
.ulDiv{
      width: 320px;
      justify-content: center;
  }
  .ulDiv li{
      width:280px;
      font-size: 14px ;
      
     
      
      
  }
  .updateDiv{
    width: 290px;
    height:270px;
   
  }
  .updateDiv input{
    
    width:270px;
    height:30px;
   
    
  }
}
 @media screen and (max-width:415px){
    .container{
      width:300px;
  }
  .inputDiv{
      width:290px;
}
.ulDiv{
      width: 300px;
      justify-content: center;
  }
  .ulDiv li{
      width:260px;
      font-size: 13px ;
      
     
      
      
  }
  .updateDiv{
    width: 270px;
    height:250px;
   
  }
  .updateDiv input{
    
    width:250px;
    height:30px;
   
    
  }
}
}

  </style>
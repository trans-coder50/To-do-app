<template>

<form action="" method="post" @submit.prevent="login" class="formlogin">
  <div>
<label for="username">User name</label><br>
<input type="text" name="" id="username" v-model="username" >
  </div>
<div>
<label for="password">Password</label><br>
<input type="password" name="" id="password" v-model="password">
</div>

<button type="submit">Login</button>
<router-link to="/signup" class="signuplink">Create an account</router-link>
</form>


</template>

<script>
import jwt_decode from "jwt-decode"
export default {
    name:'signin',
    data(){
  return{
    username:'',
    password:''
  }
},

methods:{
  async login() {
        let response =await fetch('http://127.0.0.1:8000/token/',
      {
        method:'POST',
        headers:{
          'Content-Type':'application/json',
        },
        body:JSON.stringify({"username":this.username, "password":this.password})
     
      })
      let data = await response.json()
      if(response.status === 200){
          this.$store.state.authTokens = data.access
          let authInfo = jwt_decode(data.access)
          this.$store.state.authInfo = authInfo
          localStorage.setItem('authTokens', JSON.stringify(data))
          this.$router.push('/')
          
      }

   }
}
}

</script>


<style>
.formlogin{
  width:100vw;
  height:100vh;
  display:flex;
  justify-content: center;
  align-items:center;
flex-direction: column;
}
.formlogin div{
  width:350px;
  margin: 5px;
  display:flex; 
  flex-direction: column;
  align-items: flex-start;
  
}
.formlogin input{
width:350px;
    height:30px;
    border-radius: 5px;
      color:rgb(226, 221, 221);
      border:none;
      margin-bottom:10px;
      background:#40414F;
      margin-top:5px
}
.formlogin label{
    color:rgb(226, 221, 221);
    font-size: 23px;
}
.formlogin button{
   color:#2B2A31;
    background: #FAE69E;
    border:none;
    width:100px;
    height:32px;
    border-radius:7px;
    font-size:18px;
    font-weight:normal;
    margin-bottom: 20px;
}
.signuplink{
  text-decoration:none;
  color:rgb(226, 221, 221);
  font-size: 20px;
}
.signuplink:hover{
  color:#FAE69E
}
</style>
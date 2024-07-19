<template>
<form  method="post" @submit.prevent="registerUser" class="formsignup">
    
    <div>
    <label for="email">Email</label>
    <input type="email" name="" id="email" v-model="email">
    </div>
    <div>
  <label for="username">User name</label>
    <input type="text" name="" id="username" v-model="username">
    </div>
    <div>
      <label for="password">Password</label>
    <input type="password" name="" id="password" v-model="password">
    </div>
    
    <div>
      <label for="password2">Password</label>
    <input type="password" name="" id="password2" v-model="password2">
    </div>
    <button type="submit">Signup</button>
    <router-link to="/signin" class="signinlink">You already have an account</router-link>
</form>

</template>

<script>

import axios from 'axios'

export default {
    name:'SignUpView',
data(){
    return{
        email:'',
        username:'',
        password:'',
        password2:'',
    }
},
methods: {
  registerUser() {
      const data = {
        username: this.username,
        email: this.email,
        password: this.password,
        password2: this.password2,
      };
   axios.post('http://127.0.0.1:8000/register/', data)
        .then(response => {
          this.$router.push({name:'signin'})
        })
        .catch((error)=>{
           console.log(error)})
  },
 
 }

}
</script>

<style>
.formsignup{
  width:100vw;
  height:100vh;
  display:flex;
  justify-content: center;
  align-items:center;
flex-direction: column;
}
.formsignup div{
  width:350px;
  margin: 5px;
  display:flex; 
  flex-direction: column;
  align-items: flex-start;
  
}
.formsignup input{
width:350px;
    height:30px;
    border-radius: 5px;
      color:rgb(226, 221, 221);
      border:none;
      margin-bottom:10px;
      background:#40414F;
      margin-top:5px
}
.formsignup label{
    color:rgb(226, 221, 221);
    font-size: 23px;
}
.formsignup button{
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
.signinlink{
  text-decoration:none;
  color:rgb(226, 221, 221);
  font-size: 20px;
}
.signinlink:hover{
  color:#FAE69E
}
</style>
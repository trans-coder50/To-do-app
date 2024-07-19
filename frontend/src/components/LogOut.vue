<template>
  <button @click="logout" class="logout">Logout</button>
  <svg  @click="logout" xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="#FAE69E" class="bi bi-box-arrow-right logoutsvg" viewBox="0 0 16 16">
  <path fill-rule="evenodd" d="M10 12.5a.5.5 0 0 1-.5.5h-8a.5.5 0 0 1-.5-.5v-9a.5.5 0 0 1 .5-.5h8a.5.5 0 0 1 .5.5v2a.5.5 0 0 0 1 0v-2A1.5 1.5 0 0 0 9.5 2h-8A1.5 1.5 0 0 0 0 3.5v9A1.5 1.5 0 0 0 1.5 14h8a1.5 1.5 0 0 0 1.5-1.5v-2a.5.5 0 0 0-1 0v2z"/>
  <path fill-rule="evenodd" d="M15.854 8.354a.5.5 0 0 0 0-.708l-3-3a.5.5 0 0 0-.708.708L14.293 7.5H5.5a.5.5 0 0 0 0 1h8.793l-2.147 2.146a.5.5 0 0 0 .708.708l3-3z"/>
</svg>
</template>

<script>
export default {
    name:"logout",
    methods:{
    logout(){
      localStorage.removeItem('authTokens')
      window.location.href = '/signin'
      
    }
  }

}
</script>

<style>
.logout{
  position:absolute;
  left:0px;
  top:10px;
  margin:10px;
   height:35px;
    width:90px;
    background: #FAE69E;
    border-radius:10px;
    font-size:20px;
    font-weight: 500;
    color:#2B2A31;
  border:none;
}
.logoutsvg{display:none}

@media screen and (max-width:630px){
   .logout{
  display:none
}
.logoutsvg{
  cursor: pointer;
  display:block;
  position:absolute;
  left:0px;
  top:10px;
  margin:10px;
}
}
</style>
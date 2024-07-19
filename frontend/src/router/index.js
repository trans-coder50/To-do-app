import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import SignUpView from '../views/SignUpView.vue'
import SignInView from '../views/SignInView.vue'
import pagenotfound from '../views/PageNotFound.vue'


const gaurd = function(to,from,next){
  
  if(localStorage.getItem('authTokens') ){
    next()
  }else{
    next('/signin')
  }
  }
 
const protect1 = function(to,from,next){
  if(localStorage.getItem('authTokens')){
    next('/')
  }else{
    next()
  }
}
const protect2 = function(to,from,next){
  if(localStorage.getItem('authTokens')){
    next('/')
  }else{
    next()
  }
}
const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
    beforeEnter:(to,from,next)=>{gaurd(to,from,next)}
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignUpView,
    beforeEnter:(to,from,next)=>{protect1(to,from,next)}
  },
   {
    path: '/signin',
    name: 'signin',
    component: SignInView,
    beforeEnter:(to,from,next)=>{protect2(to,from,next)}

  },
  {
    path: '/:catchAll(.*)',
    name: 'pagenotfound',
    component: pagenotfound,
  }
 

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router

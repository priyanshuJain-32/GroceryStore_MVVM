import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const routes = [
  {path: '/', name: 'home', component: HomeView},
  {path: '/about', name: 'about', component: () => import('../views/AboutView.vue')},
  {path: '/signup', name: 'signup', component: () => import('../views/SignUpView.vue')},
  {path: '/login', name: 'login', component: () => import('../views/LoginView.vue')},
  {path: '/adminlogin', name: 'adminlogin', component: () => import('../views/LoginView.vue')}
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router

import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const routes = [
  {path: '/', name: 'home', component: HomeView},
  {path: '/about', name: 'about', component: () => import('../views/AboutView.vue')},
  {path: '/signup', name: 'signup', component: () => import('../views/SignUpView.vue')},
  {path: '/login', name: 'login', component: () => import('../views/LoginView.vue')},
  {path: '/logout', name: 'logout', component: () => import('../views/LogoutView.vue')},
  {path: '/admin-login', name: 'admin-login', component: () => import('../views/LoginView.vue')},
  {path: '/categories-user-view', name: 'categories-user-view', component: () => import('../views/CategoriesView.vue')},
  {path: '/products-user-view/', name: 'products-user-view', component: () => import('../views/ProductsView.vue')},
  {path: '/buy-now-user-view/:product_id', name: 'buy-now-user-view', component: () => import('../views/BuyNowUserView.vue')},
  {path: '/cart-user-view', name: 'cart-user-view', component: () => import('../views/CartUserView.vue')},
  {path: '/orders-user-view', name: 'orders-user-view', component: () => import('../views/OrdersUserView.vue')}
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router

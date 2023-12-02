import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const routes = [

  // General routes
  {path: '/', name: 'home', component: HomeView},
  {path: '/about', name: 'about', component: () => import('../views/AboutView.vue')},
  {path: '/logout', name: 'logout', component: () => import('../views/LogoutView.vue')},
  {path: '/signup', name: 'signup', component: () => import('../views/SignUpView.vue')},
  {path: '/login', name: 'login', component: () => import('../views/LoginView.vue')},

  // User routes
  {path: '/categories-user-view', name: 'categories-user-view', component: () => import('../views/CategoriesView.vue')},
  {path: '/products-user-view/', name: 'products-user-view', component: () => import('../views/ProductsView.vue')},
  {path: '/buy-now-user-view/:product_id', name: 'buy-now-user-view', component: () => import('../views/BuyNowUserView.vue')},
  {path: '/cart-user-view', name: 'cart-user-view', component: () => import('../views/CartUserView.vue')},
  {path: '/orders-user-view', name: 'orders-user-view', component: () => import('../views/OrdersUserView.vue')},

  // Staff routes
  {path: '/admin-login', name: 'admin-login', component: () => import('../views/LoginView.vue')},
  {path: '/products-staff-view', name: 'products-staff-view', component: () => import('../views/ProductsView.vue')},
  {path: '/dashboard-staff-view', name: 'dashboard-staff-view', component: () => import('../views/DashboardStaffView.vue')},
  {path: '/add-product-view', name: 'add-product-view', component: () => import('../views/AddProductView.vue')},
  {path: '/delete-product-view/:product_id', name: 'delete-product-view', component: () => import('../views/DeleteProductView.vue')},
  {path: '/edit-product-view/:product_id', name: 'edit-product-view', component: () => import('../views/EditProductView.vue')},
  {path: '/edit-category-view/:category_id', name: 'edit-category-view', component: () => import('../views/EditCategoryView.vue')},
  {path: '/delete-category-view/:category_id', name: 'delete-category-view', component: () => import('../views/DeleteCategoryView.vue')},
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router

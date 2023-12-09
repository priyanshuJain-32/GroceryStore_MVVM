<template>
  <nav>
    |
    <router-link v-if="token.jwt == ''" to="/"> | Home | </router-link>
    <router-link v-if="token.jwt == ''" to="/about"> | About | </router-link>
    <router-link @click="setUserRole('user')" v-if="token.jwt == ''" to="/login"> | User Login | </router-link>
    <router-link @click="setUserRole('user')" v-if="token.jwt == ''" to="/signup"> | Sign Up | </router-link>
    <router-link @click="setUserRole('admin')" v-if="token.jwt == ''" to="/admin-login">| Staff Login | </router-link>
    <router-link v-if="(token.jwt !== '') && (params.role=='manager' || params.role=='admin')" to="/dashboard-staff-view"> | Dashboard | </router-link>
    <router-link v-if="token.jwt !== '' && (params.role=='manager' || params.role=='admin')" to="/categories-user-view"> | All Categories | </router-link>
    <router-link v-if="token.jwt !== '' && params.role == 'user'" to="/products-user-view/"> | Products | </router-link>
    <router-link v-if="(token.jwt !== '') && (params.role=='manager' || params.role=='admin')" to="/products-staff-view"> | Products | </router-link>
    <router-link v-if="token.jwt !== '' && params.role == 'user'" to="/cart-user-view"> | Cart | </router-link>
    <router-link v-if="token.jwt !== '' && params.role == 'user'" to="/orders-user-view"> | Orders | </router-link>
    <router-link @click="logout()" v-if="token.jwt !== ''" to="/logout">| Logout |</router-link>
    |
  </nav>
  <router-view/>
</template>

<script>
import { mapGetters, mapActions, mapMutations } from 'vuex';
export default {
  name: 'App',
  computed: {
    ...mapGetters('auth',['token', 'params'])
  },
  methods: {
    ...mapActions('auth',['logout']),
    ...mapMutations('auth',['setUserRole'])
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
  text-decoration: none;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>

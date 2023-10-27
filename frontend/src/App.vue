<template>
  <nav>
    |
    <router-link v-if="token.jwt == ''" to="/"> | Home | </router-link>
    <router-link to="/about"> | About | </router-link>
    <router-link v-if="token.jwt == ''" to="/login"> | User Login | </router-link>
    <router-link v-if="token.jwt == ''" to="/signup"> | Sign Up | </router-link>
    <router-link v-if="token.jwt == ''" to="/admin-login">| Admin Login | </router-link>
    <router-link v-if="token.jwt !== ''" to="/products-user-view"> | Products | </router-link>
    |
  </nav>
  <router-view/>
</template>

<script>
import { mapGetters } from 'vuex';
export default {
  name: 'App',
  computed: {
    ...mapGetters('auth',['token'])
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

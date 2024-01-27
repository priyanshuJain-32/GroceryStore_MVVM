<template>
  <div class="home">
    <nav>
    <div v-if="params.role == 'admin'">
      <router-link @click="setUserRole('manager')" to="/signup"> | Manager SignUp | </router-link>
      <router-link @click="setUserRole('manager')" to="/login"> | Manager Login | </router-link>
    </div>
  </nav>
    <LoginInput/>
    <br><br>
    <button type="button" @click="loginUser()">Login</button>
  </div>
</template>

<script>
// @ is an alias to /src
import LoginInput from '@/components/LoginInput.vue'
import { mapGetters, mapMutations, mapActions } from 'vuex';

export default {
  name: 'LoginView',
  components: {
    LoginInput
  },
  computed: {
    ...mapGetters('auth',['params'])
  },
  methods: {
    ...mapMutations('auth',['setUserRole']),
    ...mapActions('auth',['loginUser'])
  }
}
</script>

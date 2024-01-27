<template>
  <div class="signup">
    <SignupInput/>
  </div>
</template>

<script>
// @ is an alias to /src
import SignupInput from '@/components/SignupInput.vue'

export default {
  name: 'SignUpView',
  components: {
    SignupInput
  }
}
</script>

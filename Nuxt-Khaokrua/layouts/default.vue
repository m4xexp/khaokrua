<template>
  <v-app light style="background-color: #e4e5e5">
      <Nav v-if="$store.getters.getNavDefaultState"/>  
      <NavLogin v-if="$store.getters.getNavLoginState" />
      <!--  -->
      <!-- v-if="$store.getters.getNavLoginState" -->
    <v-main>
      <v-overlay :value="this.$store.getters.getLoadingState">
        <v-progress-circular
          indeterminate
          size="64"
        ></v-progress-circular>
      </v-overlay>
      <nuxt />
    </v-main>
    <v-footer app>
      <span>&copy; {{ new Date().getFullYear() }}</span>
    </v-footer>
  </v-app>
</template>

<script>

import Nav from '../components/Core/Nav'
import NavLogin from '../components/Core/NavLogin'
import NavLogSearch from '../components/Core/NavLogSearch'

export default {
  components: { Nav, NavLogin, NavLogSearch},

  data() {
    return {
      
    }
  },
  
  mounted() {
    this.$store.dispatch({ type: "restoreLogin" });
    var token = this.$store.getters.getUserID
    console.log('token',token)
    var homeNav = this.$store.getters.getNavDefaultState
    console.warn('Hove Nav',homeNav)

  }
}
</script>

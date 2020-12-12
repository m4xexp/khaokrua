<template>
  <v-app dark style="background-color: #e4e5e5">
    <PageNotFound v-if="error.statusCode === 404"/>

    <h1 v-else>
      {{ otherError }}
    </h1>
  </v-app>
</template>

<script>

import PageNotFound from '../components/Core/PageNotFound';

export default {
  components: { PageNotFound },
  layout: 'empty',
  props: {
    error: {
      type: Object,
      default: null
    }
  },
  data () {
    return {
      pageNotFound: '404 Not Found',
      otherError: 'An error occurred'
    }
  },
  head () {
    const title =
      this.error.statusCode === 404 ? this.pageNotFound : this.otherError
    return {
      title
    }
  }
}
</script>

<style scoped>
h1 {
  font-size: 20px;
}
</style>

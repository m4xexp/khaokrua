import colors from 'vuetify/es5/util/colors'

export default {
  // Global page headers (https://go.nuxtjs.dev/config-head)
  head: {
    titleTemplate: '%s - khaokruanuxt',
    title: 'khaokruanuxt',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' }
    ],

    script: [
      {
        src: "https://widget.cloudinary.com/v2.0/global/all.js"
      }

    ],

    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ]
  },

  // Global CSS (https://go.nuxtjs.dev/config-css)
  css: [
  ],

  // Plugins to run before rendering page (https://go.nuxtjs.dev/config-plugins)
  plugins: [
    // '~/plugins/axios'
  ],

  // Auto import components (https://go.nuxtjs.dev/config-components)
  components: true,

  // Modules for dev and build (recommended) (https://go.nuxtjs.dev/config-modules)
  buildModules: [
    // https://go.nuxtjs.dev/vuetify
    '@nuxtjs/vuetify',
  ],

  // Modules (https://go.nuxtjs.dev/config-modules)
  modules: [
    // https://go.nuxtjs.dev/axios
    '@nuxtjs/axios',
    // https://go.nuxtjs.dev/pwa
    '@nuxtjs/pwa',
    'nuxt-material-design-icons',
    '@nuxtjs/auth',
    // '@nuxtjs/cloudinary'
  ],

  // cloudinary: {
  //   cloudName: '<your-cloud-name>'
  // },

  //https://sakko-demo-api.herokuapp.com/api/v1/user/sign_in
  auth: {
    redirect: {
      login: '/login'
    },
    strategies: {
      local: {
        endpoints: {
          login: { url: 'https://sakko-demo-api.herokuapp.com/api/v1/user/sign_in', method: 'post', propertyName: 'user.auth_jwt' },
          logout: { url: 'https://sakko-demo-api.herokuapp.com/api/v1/user/sign_out', method: 'delete' },
          user: { url: 'https://sakko-demo-api.herokuapp.com/api/v1/user/me', method: 'get', propertyName: 'user' }
        },
        tokenName: 'auth-token'
      },
    }

  },

  // Axios module configuration (https://go.nuxtjs.dev/config-axios)
  axios: {},

  // Vuetify module configuration (https://go.nuxtjs.dev/config-vuetify)
  vuetify: {
    customVariables: ['~/assets/variables.scss'],
    theme: {
      dark: false,
      themes: {
        dark: {
          primary: colors.blue.darken2,
          accent: colors.grey.darken3,
          secondary: colors.amber.darken3,
          info: colors.teal.lighten1,
          warning: colors.amber.base,
          error: colors.deepOrange.accent4,
          success: colors.green.accent3
        }
      }
    }
  },

  // Build Configuration (https://go.nuxtjs.dev/config-build)
  build: {
    // vendor: [
    //   'vue-axios' //-- add vendor vue-axios
    // ],
  },

  // proxy: {
  //   '/api': 'http://127.0.0.1:8888', //-- ตั้งค่า map proxy url api server
  //   ws: true
  // },
}

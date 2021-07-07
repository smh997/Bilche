export default {
  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    title: 'bilche-web',
    htmlAttrs: {
      lang: 'en',
      dir: 'rtl',
    },
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' },
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
      { rel: 'stylesheet', href: '/fonts/fontawesome/css/all.min.css' },
    ],
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: ['~/assets/scss/global.scss', '~/assets/css/fonts.css'],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [
    '~/plugins/vue-js-modal.client.ts',
    '~/plugins/toast.client.ts',
    '~/plugins/axios-error-handler.client.ts',
  ],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
    // https://go.nuxtjs.dev/typescript
    '@nuxt/typescript-build',
    '@nuxtjs/style-resources',
  ],
  /*
   ** styleResources module configuration
   ** See https://github.com/nuxt-community/style-resources-module
   */
  styleResources: {
    scss: ['./assets/scss/*.scss'],
  },

  env: {
    API_BASE_URL: 'http://127.0.0.1:8000/',
  },

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    // https://go.nuxtjs.dev/axios
    '@nuxtjs/axios',
  ],

  // Axios module configuration: https://go.nuxtjs.dev/config-axios
  axios: {},

  build: {
    extend(config, { isDev }) {
      if (!isDev) {
        config.module.rules.push({
          enforce: 'pre',
          test: /\.(ts|js|vue)$/,
          loader: 'eslint-loader',
          exclude: [/(node_modules)/, /api/],
        })
      }
    },
  },

  /*
   ** env variables
   ** See https://nuxtjs.org/blog/moving-from-nuxtjs-dotenv-to-runtime-config/
   */
  publicRuntimeConfig: {
    apiBaseURL: 'http://127.0.0.1:8000/',
  },
}

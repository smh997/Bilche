/* eslint-disable import/no-duplicates */
declare module 'vue-slick-carousel' {
  import Vue, { PluginFunction } from 'vue'
  export const install: PluginFunction<{}>
  export default class VueSlickCarousel extends Vue {}
}

// declare module 'v-click-outside' {
//   import { PluginFunction } from 'vue'
//   export const install: PluginFunction<{}>
// }

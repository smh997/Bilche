import Toasted from 'vue-toasted'
import Vue from 'vue'
Vue.use(Toasted, {
  containerClass: 'toast-container',
  className: 'toast',
  iconPack: 'fontawesome',
  type: 'error',
  icon: 'times',
  position: 'top-left',
  duration: 5000,
})

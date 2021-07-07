import axios, { AxiosError } from 'axios'
import Vue from 'vue'

axios.interceptors.response.use(
  function (response) {
    return response
  },
  function (error: AxiosError) {
    if (error.response) {
      if (error?.response?.status !== 401 && error?.response?.status !== 403) {
        if (error.response.data.error) {
          Vue.toasted.error(error.response.data.error)
        } else {
          Vue.toasted.error('خطا !')
        }
      }
    }
    return Promise.reject(error)
  }
)

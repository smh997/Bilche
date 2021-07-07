import axios, { AxiosError } from 'axios'
import Vue from 'vue'

axios.interceptors.response.use(
  function (response) {
    return response
  },
  function (error: AxiosError) {
    if (error.response) {
      if (error?.response?.status !== 401 && error?.response?.status !== 403) {
        if (error.response.data.errors) {
          const errors = error.response.data.errors as string[]
          errors.forEach((error) => {
            Vue.toasted.error(error)
          })
        } else {
          Vue.toasted.error('خطا !')
        }
      }
    }
    return Promise.reject(error)
  }
)

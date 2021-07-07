import Vue from 'vue'
import { ModuleAccessor, Module, mutation } from 'vuex-module-accessor'

// api
import { ApiApi, InstallappApplicationStoreEnum } from '~/api'

// libs
import {
  phoneNumberValidation,
  validateEmail,
} from '~/lib/types/utils/validations'

const api = new ApiApi()

class HomeState {
  newsLetterMobileEmailValid: boolean = true
  survayEmailValid: boolean = true
}

export class HomeModule extends Module<HomeState> {
  constructor() {
    super(HomeState)
  }

  /** ***************************** mutations ********************************* */
  set mobileEmailValid(mobileEmailValid: boolean) {
    this.state.newsLetterMobileEmailValid = mobileEmailValid
  }

  get mobileEmailValid(): boolean {
    return this.state.newsLetterMobileEmailValid
  }

  set survayEmailValid(survayEmailValid: boolean) {
    this.state.survayEmailValid = survayEmailValid
  }

  get survayEmailValid(): boolean {
    return this.state.survayEmailValid
  }

  /** **************************** validations ******************************** */
  @mutation
  newsLetterInputValidation(mobileEmail: string) {
    this.state.newsLetterMobileEmailValid =
      phoneNumberValidation(mobileEmail) || validateEmail(mobileEmail)
  }

  @mutation
  survayEmailValidation(email: string) {
    this.state.survayEmailValid = validateEmail(email)
  }

  /** *************************** actions ************************************* */
  async newsLetterSubscribe(mobileEmail: string) {
    try {
      await api.createSubscribe({ email_phone: mobileEmail })
      Vue.toasted.success('خوشحالیم که به جمع ما ملحق شدی!')
    } catch (err) {}
  }

  async submitFeedback(payload: {
    fullName?: string
    email?: string
    comment: string
  }) {
    try {
      await api.createFeedback({
        fullname: payload.fullName,
        email: payload.email,
        text: payload.comment,
      })
      Vue.toasted.success('ممنون که نظرت رو با بیلچه به اشتراک گذاشتی!')
    } catch (err) {}
  }

  async download(link: InstallappApplicationStoreEnum) {
    try {
      await api.createInstallapp({ application_store: link })
    } catch (err) {}
  }
}

export default new ModuleAccessor(new HomeModule(), 'home/')

import Vue from 'vue'
// import { v4 as uuidv4 } from 'uuid'
import { ModuleAccessor, Module, mutation } from 'vuex-module-accessor'

// lib
import {
  phoneNumberValidation,
  validateEmail,
} from '~/lib/types/utils/validations'

// apis
import { ApiApi } from '~/api'
const api = new ApiApi()

// types
export type Token = string | null
class AuthState {
  token: Token = null
  // phonenumber
  phoneNumber: string | null = ''
  showLoginModal: boolean = false
  isPhoneNumberValid: boolean = true
  // firstName
  name: string = ''
  nameValid: boolean = true
  // password
  password: string = ''
  passwordValid: boolean = true
  // email
  email: string = ''
  emailValid: boolean = true
  // valid
  allValid: boolean = true
  // user uuid
  // uuid: string | null = null
}

export class AuthModule extends Module<AuthState> {
  constructor() {
    super(AuthState)
  }

  /**
   * set uuid for each user
   *
   * @memberof AuthModule
   */
  @mutation
  setUUID() {
    if (process.client) {
      // const uuid = localStorage.getItem('uuid') || uuidv4()
      // this.state.uuid = uuid
      // localStorage.setItem('uuid', uuid)
    }
  }

  /**
   *	set token (from props or localStorage)
   *
   * @memberof AuthModule
   */
  @mutation
  setToken(token?: Token) {
    if (process.client) {
      if (token !== undefined) {
        if (token) {
          const expire = new Date()
          expire.setDate(expire.getDate() + 1)
          localStorage.setItem('token', token)
          localStorage.setItem('tokenExpireDate', expire.toISOString())
          this.state.token = token
        } else {
          localStorage.removeItem('token')
          localStorage.removeItem('tokenExpireDate')
          this.state.token = null
        }
      } else {
        const tokenExpireDate = localStorage.getItem('tokenExpireDate')
        if (
          tokenExpireDate &&
          new Date(tokenExpireDate).getTime() > new Date().getTime()
        ) {
          this.state.token = localStorage.getItem('token')
        } else {
          localStorage.removeItem('token')
          localStorage.removeItem('tokenExpireDate')
          this.state.token = null
        }
      }
    }
  }

  set showLoginModal(is: boolean) {
    this.state.showLoginModal = is
  }

  get showLoginModal(): boolean {
    return this.state.showLoginModal
  }

  /**
   * set user phone number
   *
   * @memberof AuthModule
   */
  set phoneNumber(phoneNumber: string | null) {
    if (!this.state.isPhoneNumberValid) {
      // this.state.isPhoneNumberValid = phoneNumberValidation(phoneNumber)
    }
    this.state.phoneNumber = phoneNumber
  }

  get phoneNumber(): string | null {
    return this.state.phoneNumber
  }

  /**
   *
   *
   * @memberof AuthModule
   */
  set isPhoneNumberValid(isPhoneNumberValid: boolean) {
    this.state.isPhoneNumberValid = isPhoneNumberValid
  }

  get isPhoneNumberValid(): boolean {
    return this.state.isPhoneNumberValid
  }

  /**
   *	set user first name
   *
   * @memberof AuthModule
   */
  set name(name: string) {
    this.state.name = name
  }

  get name(): string {
    return this.state.name
  }

  /**
   *	set user pass for login
   *
   * @memberof AuthModule
   */
  set password(password: string) {
    this.state.password = password
  }

  get password(): string {
    return this.state.password
  }

  set passwordValid(passwordValid: boolean) {
    this.state.passwordValid = passwordValid
  }

  get passwordValid(): boolean {
    return this.state.passwordValid
  }

  set email(email: string) {
    this.state.email = email
  }

  get email(): string {
    return this.state.email
  }

  set emailValid(emailValid: boolean) {
    this.state.emailValid = emailValid
  }

  get emailValid(): boolean {
    return this.state.emailValid
  }

  @mutation
  private resetState() {
    this.state.phoneNumber = ''
    this.state.isPhoneNumberValid = true
    this.state.name = ''
    this.state.nameValid = true
    this.state.password = ''
    this.state.passwordValid = true
    this.state.email = ''
    this.state.emailValid = true
    this.state.allValid = true
  }

  /* ************************************  validations ************************************** */

  /**
   *	check register form validation
   *
   * @memberof AuthModule
   */
  @mutation
  private checkRegisterForm() {
    this.state.allValid = true
    this.state.passwordValid = true
    this.state.emailValid = true
    this.state.isPhoneNumberValid = true

    if (this.state.password === '') {
      this.state.passwordValid = false
      this.state.allValid = false
    }
    if (!validateEmail(this.state.email)) {
      this.state.emailValid = false
      this.state.allValid = false
    }
    if (this.state.phoneNumber && this.state.phoneNumber.length > 0) {
      if (!phoneNumberValidation(this.state.phoneNumber)) {
        this.state.isPhoneNumberValid = false
        this.state.allValid = false
      }
    }
  }

  /**
   *	check register form validation
   *
   * @memberof AuthModule
   */
  @mutation
  private checkLoginForm() {
    this.state.allValid = true
    this.state.passwordValid = true
    this.state.isPhoneNumberValid = true

    if (this.state.password === '') {
      this.state.passwordValid = false
      this.state.allValid = false
    }
    if (!validateEmail(this.state.email)) {
      this.state.emailValid = false
      this.state.allValid = false
    }
    if (this.state.phoneNumber?.length === 0) {
      this.state.phoneNumber = null
    }
  }

  /**
   *	check resetPass form validation
   *
   * @memberof AuthModule
   */
  @mutation
  private checkResetPassForm() {
    this.state.allValid = true
    this.state.passwordValid = true

    if (this.state.password === '') {
      this.state.passwordValid = false
      this.state.allValid = false
    }
  }

  /* ************************************  ajax calls ************************************** */

  /**
   *	register new user
   *
   * @memberof AuthModule
   */
  async registerUser() {
    this.checkRegisterForm()
    if (this.state.allValid) {
      try {
        await api.createUser({
          email: this.state.email,
          fullname: this.state.name,
          password: this.state.password,
          phone_number: this.state.phoneNumber,
        })
        Vue.toasted.success('از اینکه به جمع ما پیوستی خوشحالیم:)')
        // this.login()
      } catch (error) {}
    }
  }

  /**
   *	call service to login user
   *
   * @memberof AuthModule
   */
  async login() {
    this.checkLoginForm()
    if (this.state.allValid) {
      try {
        const response = await api.createMyAuthToken({
          username: this.state.email,
          password: this.state.password,
        })
        this.setToken(response.data.token)
        this.resetState()
      } catch (error) {}
    }
  }

  /**
   *	call service to login user
   *
   * @memberof AuthModule
   */
  async sendResetPasswordToken() {
    this.emailValid = true
    if (validateEmail(this.state.email)) {
      try {
        await api.createEmail({
          email: this.state.email,
        })
      } catch (error) {}
    } else {
      this.emailValid = false
    }
  }

  /**
   *	call service to reset password (forget pass)
   *
   * @memberof AuthModule
   */
  async resetPassword(payload: { token: string }) {
    if (this.state.password !== '') {
      try {
        await api.createPasswordToken({
          password: this.state.password,
          token: payload.token,
        })
        Vue.toasted.success('رمز عبور با موفقیت تغییر کرد')
        this.resetState()
      } catch (error) {}
    } else {
      this.passwordValid = false
    }
  }

  /**
   * logout user
   *
   * @memberof AuthModule
   */
  logout() {
    this.setToken(null)
  }
}

export default new ModuleAccessor(new AuthModule(), 'auth/')

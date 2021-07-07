import Vue from 'vue'
// import { v4 as uuidv4 } from 'uuid'
import { ModuleAccessor, Module, mutation } from 'vuex-module-accessor'

// lib
// import { phoneNumberValidation } from '~/lib/utils/validations'

// apis

// types
export type Token = string | null
class AuthState {
  token: Token = null
  // phonenumber
  phoneNumber: string = ''
  showLoginModal: boolean = false
  isPhoneNumberValid: boolean = true
  // firstName
  name: string = ''
  nameValid: boolean = true
  // password
  password: string = ''
  passwordValid: boolean = true
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

  /**
   * set user phone number
   *
   * @memberof AuthModule
   */
  set phoneNumber(phoneNumber: string) {
    if (!this.state.isPhoneNumberValid) {
      // this.state.isPhoneNumberValid = phoneNumberValidation(phoneNumber)
    }
    this.state.phoneNumber = phoneNumber
  }

  get phoneNumber(): string {
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

  @mutation
  private resetState() {
    this.state.phoneNumber = ''
    this.state.isPhoneNumberValid = true
    this.state.name = ''
    this.state.nameValid = true
    this.state.password = ''
    this.state.passwordValid = true
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
    this.state.nameValid = true
    this.state.passwordValid = true

    if (this.state.name === '') {
      this.state.nameValid = false
      this.state.allValid = false
    }
    if (this.state.password === '') {
      this.state.passwordValid = false
      this.state.allValid = false
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
  registerUser() {
    this.checkRegisterForm()
    if (this.state.allValid) {
      try {
        // await userSingUp.apiUsersRegisterPost({
        //   username: this.state.phoneNumber,
        //   name: this.state.name,
        //   password: this.state.password,
        //   acceptedEULA: true,
        // })
        this.login()
      } catch (error) {}
    }
  }

  /**
   *	call service to login user
   *
   * @memberof AuthModule
   */
  login() {
    // if (phoneNumberValidation(this.state.phoneNumber)) {
    try {
      // const response = await userLogin.apiUsersLoginPost({
      //   username: this.state.phoneNumber,
      //   password: this.state.password,
      // })
      // this.setToken(response.data.token)
      this.resetState()
    } catch (error) {}
    // } else {
    //   this.isPhoneNumberValid = false
    // }
  }

  /**
   *	call service to login user
   *
   * @memberof AuthModule
   */
  sendResetPasswordToken() {
    // if (phoneNumberValidation(this.state.phoneNumber)) {
    try {
      // await userLogin.apiUsersResetPasswordTokenPost({
      //   username: this.state.phoneNumber,
      // })
    } catch (error) {}
    // } else {
    this.isPhoneNumberValid = false
    // }
  }

  /**
   *	call service to reset password (forget pass)
   *
   * @memberof AuthModule
   */
  resetPassword() {
    this.checkResetPassForm()
    if (this.state.allValid) {
      try {
        // await userLogin.apiUsersResetPasswordPost({
        //   username: this.state.phoneNumber,
        //   resetToken: this.state.otpCode,
        //   newPassword: this.state.password,
        // })
        this.login()
      } catch (error) {}
    }
  }

  /**
   *	change user password
   *
   * @memberof AuthModule
   */
  changeUserPass() {
    this.checkResetPassForm()
    if (this.state.allValid) {
      try {
        // await userLogin.apiUsersChangePasswordPut({
        //   currentPassword: this.state.currentPassword,
        //   newPassword: this.state.password,
        // })
        Vue.toasted.show('رمز عبور تغییر کرد.', { type: 'success' })
        this.resetState()
      } catch (error) {}
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

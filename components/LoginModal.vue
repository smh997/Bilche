<template>
  <ig-modal v-model="showLoginModal" name="sign-up" :width="480">
    <div class="modal-header">
      <ig-icon
        type="far"
        icon="arrow-right"
        :size="32"
        color="#4D4D4D"
        style="cursor: pointer"
        @click="changeStep(false)"
      />
      <div class="modal-title">بیلچه</div>
      <ig-icon
        type="far"
        icon="times"
        :size="32"
        color="#4D4D4D"
        style="cursor: pointer"
        @click="showLoginModal = false"
      />
    </div>
    <div class="modal-body">
      <div class="body-title">
        {{ ModalTitle }}
      </div>
      <ig-input
        v-if="signUpStep === 'SignUp'"
        v-model="fullName"
        class="info-input"
        placeholder="نام و نام خانوادگی"
      />
      <ig-input
        v-model="email"
        class="info-input"
        required
        :invalid="!emailValid"
        placeholder="* پست الکترونیکی"
      />
      <ig-input
        v-if="signUpStep === 'SignUp'"
        v-model="phoneNumber"
        class="info-input"
        :invalid="!isPhoneNumberValid"
        placeholder="شماره همراه"
      />
      <ig-input
        v-if="signUpStep !== 'ChangePass'"
        v-model="password"
        class="info-input"
        required
        :invalid="!passwordValid"
        placeholder="* رمز عبور"
      />
      <ig-button
        class="modal-button"
        type="secondary"
        secondary-color="green"
        size="big"
        :loading="loading"
        @click="submit"
      >
        {{ ButtonText }}
      </ig-button>
      <div class="change-step" @click="changeStep(true)">
        {{ changeStepText }}
      </div>
    </div>
  </ig-modal>
</template>
<script lang="ts">
import Vue from 'vue'
import { typedMapState } from 'vuex-module-accessor'

// components
import IgModal from '~/components/IgModal.vue'
import IgIcon from '~/components/IgIcon.vue'
import IgInput from '~/components/IgInput.vue'
import IgButton from '~/components/IgButton.vue'

// store
import auth, { AuthModule } from '~/store/auth'

export default Vue.extend({
  name: 'LoginModal',
  components: { IgModal, IgIcon, IgInput, IgButton },
  data: () => ({
    signUpStep: 'SignUp',
    loading: false,
  }),
  computed: {
    authStore(): AuthModule {
      return auth.of(this.$store)
    },
    ...typedMapState(auth, {
      isPhoneNumberValid: (state) => state.isPhoneNumberValid,
      nameValid: (state) => state.nameValid,
      passwordValid: (state) => state.passwordValid,
      emailValid: (state) => state.emailValid,
    }),
    ModalTitle(): string {
      if (this.signUpStep === 'SignUp') {
        return 'ثبت نام'
      } else if (this.signUpStep === 'Login') {
        return 'ورود'
      } else {
        return 'تغییر رمز عبور'
      }
    },
    changeStepText(): string {
      if (this.signUpStep === 'SignUp') {
        return 'قبلا ثبت نام کرده‌اید؟ ورود'
      } else if (this.signUpStep === 'Login') {
        return 'رمز عبور خود را فراموش کرده‌اید؟ تغییر رمز عبور'
      } else {
        return ''
      }
    },
    ButtonText(): string {
      if (this.signUpStep === 'SignUp') {
        return 'ثبت نام در بیلچه'
      } else if (this.signUpStep === 'Login') {
        return 'ورود به بیلچه'
      } else {
        return 'تغییر رمز عبور'
      }
    },
    showLoginModal: {
      set(value: boolean) {
        this.authStore.showLoginModal = value
      },
      get(): boolean {
        return this.authStore.state.showLoginModal
      },
    },
    fullName: {
      set(value: string) {
        this.authStore.name = value
      },
      get(): string {
        return this.authStore.state.name
      },
    },
    phoneNumber: {
      set(value: string) {
        this.authStore.phoneNumber = value
      },
      get(): string | null {
        return this.authStore.state.phoneNumber
      },
    },
    email: {
      set(value: string) {
        this.authStore.email = value
      },
      get(): string {
        return this.authStore.state.email
      },
    },
    password: {
      set(value: string) {
        this.authStore.password = value
      },
      get(): string {
        return this.authStore.state.password
      },
    },
  },
  methods: {
    changeStep(isForward: boolean) {
      if (this.signUpStep === 'SignUp') {
        isForward ? (this.signUpStep = 'Login') : (this.signUpStep = 'SignUp')
      } else if (this.signUpStep === 'Login') {
        isForward
          ? (this.signUpStep = 'ChangePass')
          : (this.signUpStep = 'SignUp')
      } else {
        this.signUpStep = 'Login'
      }
    },
    submit() {
      this.loading = true
      if (this.signUpStep === 'SignUp') {
        this.authStore.registerUser()
      } else if (this.signUpStep === 'Login') {
        this.authStore.login()
      } else {
        this.authStore.sendResetPasswordToken()
      }
      this.loading = false
    },
  },
})
</script>
<style lang="scss" scoped>
.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 24px 32px 36px 32px;
  .modal-title {
    font-weight: bold;
    font-size: 43px;
    line-height: 73px;
    /* Primary/Main */
    color: #27ae60;
  }
}
.modal-body {
  padding: 0px 24px 34px 24px;
  .body-title {
    font-weight: 500;
    font-size: 19px;
    line-height: 32px;
    text-align: right;
    color: #000000;
    margin-bottom: 24px;
  }
  .change-step {
    font-weight: 500;
    font-size: 16px;
    line-height: 27px;
    /* Primary/Main */
    color: #27ae60;
    cursor: pointer;
  }
  .modal-button {
    width: 100%;
    margin-bottom: 10px;
    font-size: 22px !important;
  }
}
</style>

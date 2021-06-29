<template>
  <ig-modal name="sign-up" :value="showSignUpModal" :width="480">
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
        @click="showSignUpModal = false"
      />
    </div>
    <div class="modal-body">
      <div class="body-title">
        {{ ModalTitle }}
      </div>
      <ig-input
        v-if="signUpStep === 'SignUp'"
        class="info-input"
        placeholder="نام و نام خانوادگی"
      />
      <ig-input
        v-if="signUpStep !== 'ChangePass'"
        class="info-input"
        required
        placeholder="پست الکترونیکی"
      />
      <ig-input
        v-if="signUpStep === 'SignUp'"
        class="info-input"
        required
        placeholder="شماره همراه"
      />
      <ig-input
        v-if="signUpStep !== 'ChangePass'"
        class="info-input"
        required
        placeholder="رمز عبور"
      />
      <ig-input
        v-if="signUpStep === 'ChangePass'"
        class="info-input"
        required
        placeholder="کد یکبار مصرف"
      />
      <ig-input
        v-if="signUpStep === 'ChangePass'"
        class="info-input"
        required
        placeholder="رمز عبور جدید"
      />
      <ig-button
        class="modal-button"
        type="secondary"
        secondary-color="green"
        size="big"
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

// components
import IgModal from '~/components/IgModal.vue'
import IgIcon from '~/components/IgIcon.vue'
import IgInput from '~/components/IgInput.vue'
import IgButton from '~/components/IgButton.vue'

export default Vue.extend({
  name: 'LoginModal',
  components: { IgModal, IgIcon, IgInput, IgButton },
  data: () => ({
    showSignUpModal: false,
    signUpStep: 'SignUp',
  }),
  computed: {
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

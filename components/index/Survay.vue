<template>
  <div class="survay-container">
    <img class="image desktop" src="/img/survay-image.svg" />
    <div class="inputs-container">
      <div class="title">نظرت رو به ما بگو</div>
      <div class="inputs-row">
        <ig-input
          v-model="fullName"
          label="نام:"
          placeholder="نام و نام خانوادگی"
          class="input-col6"
        />
        <ig-input
          v-model="email"
          required
          :invalid="!survayEmailValid"
          label="ایمیل:"
          placeholder="example@Bilche.com"
          class="input-col6"
        />
      </div>
      <ig-input v-model="comment" text-area placeholder="محل نوشتن نظر" />
      <ig-button
        type="secondary"
        secondary-color="green"
        size="medium"
        class="submit-btn"
        :loading="loading"
        @click="submit"
      >
        ثبت نظر</ig-button
      >
    </div>
  </div>
</template>
<script lang="ts">
import Vue from 'vue'
import { typedMapState } from 'vuex-module-accessor'

// components
import IgInput from '~/components/IgInput.vue'
import IgButton from '~/components/IgButton.vue'

// store
import home, { HomeModule } from '~/store/home'

export default Vue.extend({
  name: 'Survay',
  components: { IgInput, IgButton },
  data: () => ({
    fullName: '',
    email: '',
    comment: '',
    loading: false,
  }),
  computed: {
    homeStore(): HomeModule {
      return home.of(this.$store)
    },
    ...typedMapState(home, {
      survayEmailValid: (state) => state.survayEmailValid,
    }),
  },
  methods: {
    async submit() {
      this.loading = true
      this.homeStore.survayEmailValidation(this.email)
      if (this.survayEmailValid) {
        await this.homeStore.submitFeedback({
          fullName: this.fullName,
          email: this.email,
          comment: this.comment,
        })
      }
      this.loading = false
    },
  },
})
</script>
<style lang="scss" scoped>
.survay-container {
  padding: 50px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.inputs-container {
  width: calc(100% - 600px);
  .title {
    font-weight: bold;
    font-size: 43px;
    line-height: 73px;
    text-align: right;
    color: $gray-10;
    margin-bottom: 16px;
  }
}
.inputs-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.input-col6 {
  width: calc(50% - 25px) !important;
}
.submit-btn {
  width: 210px;
  margin-right: auto;
}
@media (max-width: 768px) {
  .survay-container {
    padding: 16px;
  }
  .inputs-container {
    width: 100%;
    .title {
      text-align: center;
    }
  }
  .submit-btn {
    margin: 0 auto;
  }
}
</style>

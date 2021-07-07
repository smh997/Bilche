<template>
  <div class="forgot-container">
    <div class="inputs-container">
      <div class="title">تغییر رمز عبور</div>
      <div class="subtitle">رمز عبور جدید را وارد کنید.</div>
      <ig-input class="info-input" required placeholder="رمز عبور" />
    </div>
    <img src="/img/forgot-password.svg" />
  </div>
</template>
<script lang="ts">
import Vue from 'vue'

// component
import IgInput from '~/components/IgInput.vue'

export default Vue.extend({
  components: { IgInput },
})
</script>
<style lang="scss">
.forgot-container {
  background: $gray-100;
  width: 100%;
  padding: 0px 8%;
  margin-top: 96px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.inputs-container {
  width: calc(100% - 626px);
  max-width: 530px;
  .title {
    font-weight: 500;
    font-size: 19px;
    line-height: 32px;
    text-align: right;
    color: #000000;
    margin-bottom: 24px;
  }
  .subtitle {
    font-size: 16px;
    line-height: 27px;
    text-align: right;
    color: #000000;
    margin-bottom: 16px;
  }
}
</style>

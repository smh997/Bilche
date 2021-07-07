<template>
  <div class="filters-container">
    <div class="filter-box">
      <div class="filter-title">دسته بندی</div>
      <div class="filter-body">
        <ig-checkbox label="گیاهان مقاوم" />
        <ig-checkbox label="آپارتمانی" />
        <ig-checkbox label="باغچه" />
        <ig-checkbox label="گلدار" />
        <ig-checkbox label="کاکتوس و ساکولنت" />
      </div>
    </div>
    <div class="filter-box">
      <div class="filter-title">سطح رسیدگی</div>
      <div class="filter-body">
        <div class="filter-row">
          <ig-checkbox label="آسان" />
          <img src="/img/easy-stars.svg" />
        </div>
        <div class="filter-row">
          <ig-checkbox label="متوسط" />
          <img src="/img/medium-stars.svg" />
        </div>
        <div class="filter-row">
          <ig-checkbox label="سخت" />
          <img src="/img/hard-stars.svg" />
        </div>
      </div>
    </div>
    <div class="filter-box">
      <div class="filter-body">
        <ig-switch label="حساسیت زا نبودن" />
        <ig-switch label="سمی نبودن" />
        <ig-switch label="نیاز به هرس کردن" />
        <ig-switch label="نیاز به مه پاشی" />
        <ig-switch label="نیاز به تمیزکاری گلدان" />
        <ig-switch label="نیاز به تمیزکاری برگ ها" />
      </div>
    </div>
    <!-- <ig-modal class="desktop" name="filters" :value="true">
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
    </ig-modal> -->
  </div>
</template>
<script lang="ts">
import Vue from 'vue'

// components
import IgCheckbox from '~/components/IgCheckbox.vue'
import IgSwitch from '~/components/IgSwitch.vue'
// import IgModal from '~/components/IgModal.vue'

export default Vue.extend({
  components: { IgCheckbox, IgSwitch },
  data: () => ({}),
})
</script>
<style lang="scss" scoped>
.filters-container {
  width: 100%;
}
.filter-box {
  width: 100%;
  margin-bottom: 16px;
  padding: 16px;
  background: $gray-100;
  border-radius: 10px;
  .filter-title {
    font-size: 16px;
    line-height: 27px;
    text-align: right;
    color: $gray-10;
    margin-bottom: 16px;
  }
  .filter-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
}
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
</style>

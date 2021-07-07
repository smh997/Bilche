<template>
  <div class="what-container">
    <div class="title">بیلچه چیست؟</div>
    <div class="subtitle">
      بیلچه یک پلتفرم جامع گل و گیاه است که در بستر آن، می‌توانید به اطلاعات
      معتبر از هر گیاه، متناسب با شرایط نگهداری خود دست پیدا کنید. همچنین بیلچه
      به شما کمک می‌کند با استفاده از آموزش‌های موجود و یک اپلیکیشن دستیار شخصی،
      به آسانی گیاه خود را پرورش دهید و از آن مراقبت کنید.
    </div>
    <div class="cards-container">
      <div v-for="(info, index) in infos" :key="index" class="card">
        <img class="image" :src="info.image" />
        <div class="card-title">
          {{ info.title }}
        </div>
        <div class="card-description">
          {{ info.description }}
        </div>
      </div>
    </div>
  </div>
</template>
<script lang="ts">
import Vue from 'vue'
export default Vue.extend({
  name: 'WhatIsBilche',
  data: () => ({
    infos: [
      {
        title: 'دانشنامه‌ی جامع گیاهان',
        description:
          'دسترسی آسان و سریع به هر نوع اطلاعات از هر گیاهی که به دنبالش هستید.',
        image: '/img/daneshname.svg',
      },
      {
        title: 'دسترس پذیری بالا',
        description:
          'گلچین و دسته بندی گیاهان بر اساس نیازهای شما و محلی که در آن قصد نگهداری از گیاه دارید.',
        image: '/img/dastresi.svg',
      },
      {
        title: 'محتوای آموزشی',
        description:
          'هرآنچه باید برای شادابی و رشد روزافزون گیاهان خود بدانید.',
        image: '/img/amoozeshi.svg',
      },
      {
        title: 'دستیار شخصی نگهداری از گیاه',
        description:
          'ابزاری برای مدیریت، یادآوری، راهنمایی و نظارت بر پرورش گیاهان شما به بهترین شکل.',
        image: '/img/dastyar.svg',
      },
    ],
  }),
})
</script>
<style lang="scss" scoped>
.what-container {
  min-height: 660px;
  width: 89%;
  margin: 0 auto;
  text-align: center;
  padding: 80px 0px;
  .title {
    font-weight: 500;
    font-size: 28px;
    line-height: 48px;
    text-align: center;
    color: $gray-10;
    margin-bottom: 20px;
  }
  .subtitle {
    font-size: 16px;
    line-height: 27px;
    text-align: center;
    color: $gray-10;
    margin-bottom: 28px;
  }
}
.cards-container {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-wrap: wrap;
  .card {
    width: 291px;
    height: 333px;
    /* Gray/White */
    background: #ffffff;
    /* card */
    box-shadow: 0px 0px 8px rgba(0, 0, 0, 0.12);
    border-radius: 10px;
    padding: 20px;
    margin: 20px;
    .image {
      width: 150px;
      height: 150px;
      margin: 0 auto;
      border-radius: 50%;
      margin-bottom: 15px;
    }
    .card-title {
      font-weight: 500;
      font-size: 16px;
      line-height: 27px;
      text-align: center;
      color: $gray-10;
      margin-bottom: 8px;
    }
  }
}
</style>

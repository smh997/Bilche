<template>
  <div class="what-container">
    <div class="title">بیلچه چیست؟</div>
    <div class="subtitle">
      لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ، و با استفاده از
      طراحان گرافیک است، چاپگرها و متون بلکه روزنامه و مجله در ستون و سطرآنچنان
      که لازم است، و برای شرایط فعلی تکنولوژی مورد نیاز، و کاربردهای متنوع با
      هدف بهبود ابزارهای کاربردی می باشد، کتابهای زیادی در شصت و سه درصد گذشته
      حال و آینده، شناخت فراوان جامعه و متخصصان را می طلبد
    </div>
    <div class="cards-container">
      <div v-for="(info, index) in infos" :key="index" class="card">
        <div class="image" />
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
        title: 'فلان است و بهمان',
        description:
          'لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ، و با استفاده از طراحان گرافیک  متنوع با',
      },
      {
        title: 'فلان است و بهمان',
        description:
          'لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ، و با، چاپگرها که لازم است،',
      },
      {
        title: 'فلان است و بهمان',
        description:
          'لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ، و با  که با',
      },
      {
        title: 'فلان است و بهمان',
        description:
          'لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ، و با استفاده متنوع با',
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
      background: #c4c4c4;
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

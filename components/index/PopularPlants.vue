<template>
  <div class="popular-container">
    <div class="title-col">
      <div class="title">گیاهان محبوب</div>
      <div class="subtitle">پرطرفدارترین گیاهان</div>
      <div class="show-button desktop">مشاهده همه</div>
    </div>
    <div class="cards-container">
      <div v-for="i in 6" :key="i" class="card">
        <img class="card-image" src="/img/big-card-image.svg" />
        <div class="card-title">کاکتوس</div>
        <div class="card-subtitle">2.4 دنبال کننده</div>
      </div>
    </div>
    <div class="show-button mobile">مشاهده همه</div>
  </div>
</template>
<script lang="ts">
import Vue from 'vue'
export default Vue.extend({
  name: 'PopularPlants',
})
</script>
<style lang="scss" scoped>
.popular-container {
  width: 100%;
  min-height: 360px;
  background: #32c770;
  padding: 50px;
  display: flex;
}
.title-col {
  margin-left: 50px;
  margin-right: 27px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  .title {
    font-weight: 500;
    font-size: 28px;
    line-height: 48px;
    text-align: right;
    color: $gray-100;
  }
  .subtitle {
    font-weight: normal;
    font-size: 16px;
    line-height: 27px;
    text-align: center;
    color: $gray-100;
    margin-bottom: 20px;
  }
}
.show-button {
  width: 100px;
  height: 40px;
  border: 1px solid $gray-100;
  border-radius: 8px;
  color: $gray-100;
  font-size: 16px;
  line-height: 27px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  margin-top: auto;
  &.mobile {
    margin: 0 auto;
    margin-top: 12px;
  }
}
.cards-container {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
}
.card {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 8px;
  width: 165px;
  height: 268px;
  background: $gray-100;
  border-radius: 8px;
  margin: 8px;
  .card-image {
    width: 149px;
    height: 192px;
    margin-bottom: 8px;
  }
  .card-title {
    font-size: 14px;
    line-height: 24px;
    color: $gray-10;
    margin-bottom: 8px;
  }
  .card-subtitle {
    font-weight: 300;
    font-size: 12px;
    line-height: 20px;
    color: $gray-10;
  }
}
@media (max-width: $app-mobile-max-width) {
  .popular-container {
    flex-direction: column;
    padding: 16px;
  }
  .cards-container {
    justify-content: center;
  }
  .title-col {
    margin-left: 0px;
    margin-right: 0px;
  }
}
</style>

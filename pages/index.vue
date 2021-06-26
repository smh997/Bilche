<template>
  <div class="home-container">
    <div class="search-header">
      <div class="search-container">
        <div class="title">بیلچه</div>
        <div class="subtitle">جستجوی گیاه، آموزش نگهداری و پرورش گیاهان</div>
        <div class="search-input-container">
          <div class="input-container"></div>
          <div class="search-button">
            <ig-icon
              class="search-icon"
              icon="search"
              color="#ffffff"
              :size="18"
            />
            جستجو
          </div>
        </div>
        <div class="classifications-container">
          <div class="title">انتخاب از دسته بندی</div>
          <div v-for="i in 5" :key="i" class="card-container">
            <img src="/img/card-image.svg" class="card-image">
            <div class="card-title">کاکتوس</div>
          </div>
        </div>
      </div>
      <img src="/img/search-header-background.svg" />
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import IgIcon from '~/components/IgIcon.vue'

export default Vue.extend({
  components: { IgIcon },
})
</script>

<style lang="scss" scoped>
.home-container {
  min-height: 100vh;
  width: 100%;
}
.search-header {
  width: 100%;
  height: 610px;
  background: #f8f9fb;
  margin-top: 90px;
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  padding: 75px;
}
.search-container {
  width: 59%;
  .title {
    font-weight: bold;
    font-size: 43px;
    line-height: 73px;
    /* Primary/Main */
    color: #27ae60;
  }
  .subtitle {
    font-weight: 500;
    font-size: 24px;
    line-height: 41px;
    margin-top: 8px;
    /* Gray/30 */
    color: #4d4d4d;
  }
  .search-input-container {
    display: flex;
    height: 70px;
    margin-top: 56px;
    .input-container {
      width: calc(100% - 210px);
      border-radius: 0px 10px 10px 0px;
      filter: drop-shadow(0px 0px 8px rgba(0, 0, 0, 0.12));
      background: white;
      height: 70px;
    }
    .search-button {
      width: 210px;
      height: 70px;
      font-weight: 500;
      font-size: 16px;
      line-height: 27px;
      display: flex;
      align-items: center;
      justify-content: center;
      /* Gray/White */
      color: #ffffff;
      /* Primary / Semi Light */
      background: #32c770;
      border-radius: 8px 0px 0px 8px;
      .search-icon {
        margin-left: 8px;
      }
    }
  }
}
.classifications-container {
  margin-top: 56px;
  display: flex;
  align-items: center;
  justify-content: flex-start;
  .title {
    margin-left: 40px;
    font-weight: 500;
    font-size: 24px;
    line-height: 41px;
    text-align: right;
    /* Gray/20 */
    color: #333333;
    max-width: 105px;
  }
  .card-container {
    width: 93px;
    padding: 8px;
    height: 133px;
    background: #ffffff;
    font-size: 14px;
    line-height: 24px;
    text-align: center;
    margin: 14px;
    /* card */
    box-shadow: 0px 0px 8px rgba(0, 0, 0, 0.12);
    border-radius: 8px;
  }
}
</style>
